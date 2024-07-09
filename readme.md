# Project README

## Overview
This project involves preprocessing and analyzing data using GPT-3.5 Turbo and GPT-4 models to extract meaningful phrases from content. Due to GPU constraints, fine-tuning of the LLaMA7b model was not feasible on Google Colab.

## Approach
My approach was straightforward:

1. **Data Preprocessing:**
   - Removed rows where content or reasons were absent, leaving 58 usable rows.
   - Filtered out rows containing `<AUDIO_CONTENT>` and summaries with insufficient information.
   - Converted content into a record class to manage data with claims, metadata, and content.
   - Removed content within angular brackets and emojis mentioned with colons to clean unwanted characters.

2. **Data Preparation:**
   - Transformed the dataframe into a list of record objects for easier manipulation.
   
3. **Phrase Extraction Using GPT-3.5 Turbo:**
   - Utilized GPT-3.5 Turbo to extract phrases directly from content rather than relying on indices.
   - Selected diverse samples and leveraged GPT-4 for more refined results.
   - Used these results as examples for the original prompt, improving GPT-3.5 Turbo's understanding.



4. **Model Fine-Tuning Attempt:**
   - Developed a script for fine-tuning the LLaMA7b model, intending to enhance performance despite limited data.
   - Due to GPU limitations on Google Colab, fine-tuning couldn't be completed.

5. **Future Work:**
   - Plan to augment the dataset to increase data diversity and improve model performance.
### Methodology

In my method, I provide the LLM with the content and one claim at a time. It generates a list of all occurrences of phrases related to the particular claim. I ensured that no line is repeated in the output array.

In an extra step, I also used LLM to evaluate the responses to determine which ones were good and bad. Using a scale of 0-5, I obtained an average score of 4.5, which was quite satisfactory.


## Scripts
- **Fine-tuning Script:** Contains the script for fine-tuning the LLaMA7b model, designed for future use with expanded data.

## Notes
- This project highlights the use of advanced language models for data analysis and the challenges faced with GPU constraints in cloud environments like Google Colab.

## Challenges Faced

The project encountered several challenges:

- **Limited Dataset and Data Understanding:**
  - Initially faced issues due to the dataset's limited size and understanding where the important and rich data resided.

- **Difficulty with Indices and Prompt Structure:**
  - Spent considerable time struggling with obtaining indices and found that the model struggled with accurately finding indices from the prompt.
  - Instead, retrieved exact portions used to back claims using regex queries from the content due to subtle changes in the model's output.
  - Required trial and error as exact matches didn't always suffice.

- **Setting up the Right Prompt:**
  - The most significant challenge involved setting up an effective prompt.
  - Adding a chain of thought significantly aided the model's performance.
