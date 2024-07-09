import pandas as pd
import re
from pprint import pformat
from typing import List, Dict

class Record:
    def __init__(self, claims: str, content: str, metadata: Dict[str, any]) -> None:
        """
        Initialize a Record object.

        Args:
            claims (str): Raw claims as a comma-separated string.
            content (str): Raw content of the record.
            metadata (Dict[str, any]): Metadata associated with the record.
        """
        self.raw_claims = claims
        self.claims = list(self.raw_claims.split(','))
        self.raw_content = content
        self.metadata = metadata
        self.instances = []
    
    def pre_process_content(self) -> None:
        """
        Pre-processes the raw content by removing angular brackets and newline characters.
        """
        # Remove all content within angular brackets
        angular_brackets_pattern = re.compile(r'<.*?>')
        self.content = re.sub(angular_brackets_pattern, '', self.raw_content)
        
        # Remove newline characters
        newline_pattern = re.compile(r'\n')
        self.content = re.sub(newline_pattern, ' ', self.content)
        
    def split_content(self) -> None:
        """
        Splits the content by keywords "User:" and "Agent:" and combines them.
        """
        # Split the content by the keywords "User:" and "Agent:"
        split_pattern = re.compile(r'(User:|Agent:)')
        segments = re.split(split_pattern, self.content)
        
        # Combine the keyword with its corresponding content
        combined_segments = []
        for i in range(1, len(segments), 2):
            combined_segments.append(segments[i] + ' ' + segments[i + 1].strip())

        self.split_content = combined_segments

    def __str__(self) -> str:
        """
        String representation of the Record object.
        """
        output = f"Content: {self.content}\nInstances:\n"
        for instance in self.instances:
            output += f"{instance['claim']}:\n{pformat(instance['instances'])}\n"
        return output
    
def create_records(df: pd.DataFrame) -> List[Record]:
    """
    Creates a list of Record objects from a pandas DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame containing columns 'Reasons', 'Content', 'ID', 'Source', 'Type', and 'Summary'.

    Returns:
        List[Record]: A list of Record objects.
    """
    records = []
    for index, row in df.iterrows():
        claims = row['Reasons']
        content = row['Content']
        metadata = {
            'ID': row['ID'],
            'Source': row['Source'],
            'Type': row['Type'],
            'Summary': row['Summary']
        }
        
        record = Record(claims, content, metadata)
        record.pre_process_content()
        record.split_content()
        
        records.append(record)

    return records
