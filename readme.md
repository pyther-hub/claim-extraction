# Project README

## Overview
The project focuses on preprocessing and analyzing conversations between a User and an Agent, utilizing GPT-3.5 Turbo and GPT-4 models to extract relevant phrases. Fine-tuning the LLaMA7b model wasn't possible on Google Colab due to GPU limitations.

## Approach

1. **Data Preprocessing:**
   - Filtered out rows containing `<AUDIO_CONTENT>` in content section because only the summaries were not having sufficient information.
   - Transformed each row into a record class object, which facilitated better data management by organizing claims, metadata, and content. This approach also allowed me to store results/extracted phrases as attributes within each data point.
   - Removed content within angular brackets and emojis mentioned with colons to clean unwanted characters.
   - Removed rows where content or reasons were absent, leaving 58 usable rows.

2. **Data Preparation:**
   - Transformed the dataframe into a list of record objects for easier manipulation.
   
3. **Phrase Extraction Using GPT-3.5 Turbo:**
   - Utilized GPT-3.5 Turbo to extract phrases directly from content rather than relying on indices. 
      - Since the model's index outputs were inconsistent, it occasionally succeeded but often failed. The model lacks inherent counting capabilities as it primarily excels in generating language only.
   - Initially, I obtained results from GPT-3.5, which assisted me in selecting diverse samples for few-shot prompting. Later, I utilized GPT-4 for more precise results, opting not to use it extensively to avoid depleting credits.
   - Used these results as examples for the original prompt, improving GPT-3.5 Turbo's understanding.
   - I utilized a regex query to search for the phrase within the content.



4. **Model Fine-Tuning Attempt:**
   - Developed a script for fine-tuning the LLama-2 7b model, intending to enhance performance.
   - Due to GPU limitations on Google Colab, fine-tuning couldn't be completed.
   - I Planed to augment the dataset to increase data diversity and improve model performance for finetuning.

   
### Methodology

In my method, I provide the LLM with the content and one claim at a time. It generates a list of all occurrences of phrases related to the particular claim. I ensured that no line is repeated in the output array.

In an extra step, I also used LLM to evaluate the responses to determine which ones were good and bad. Using a scale of 0-5, I obtained an average score of 4.5, which was quite satisfactory.


## Scripts

- **evaluate:** This evaluation script utilizes another LLM to assess the relevance of extracted phrases to the content and the mentioned claim. It returns explanations and scores in JSON format.

- **get indices:** This has the function which helps in finding the exact match of the phrase in the content.

- **get result:** This contains functions, designed to iterate over the dataset to retrieve model responses using various prompts, as explained earlier.

- **Gpt_model:** Here, I've stored the GPT models used for extracting phrases. I've also structured this entire script to allow for easy integration of other LLMs in the future, such as custom fine-tuned models deployed on a server.

- **Preprocess:** This script includes all the preprocessing steps I am using, along with the record class for efficiently storing the entire dataset.

- **Prompts:** Having all the prompts stored in one place within this script allows for quick and efficient updates when needed.

- **Fine-tuning Script:** Contains the script for fine-tuning the LLaMA7b model, designed for future use with expanded data.


## Challenges Faced

The project encountered several challenges:

- **Limited Dataset and Data Understanding:**
  -Initially, I had to drop a significant amount of content due to NaN values. I also manually reviewed the dataset to identify and remove unwanted characters, such as `<MAILTO>` tags and emojis.

- **Difficulty with Indices and Prompt Structure:**
  - Spent considerable time struggling with obtaining indices and found that the model struggled with accurately finding indices from the prompt.
  - Instead, I retrieved specific portions of the phrases that referenced the particular claim. Using regex queries, I identified the start and end indexes, although achieving an exact match was challenging due to subtle changes made by the model, resulting in a few missing characters.
  - Required trial and error as exact matches didn't always suffice.

- **Setting up the Right Prompt:**
  - The most significant challenge involved setting up an effective prompt.
  - Adding a chain of thought significantly aided the model's performance.

- **GPU constarint:**
  - I couldn't fine-tune the LLaMA model further for better inference due to the limited resources provided by Colab.
  - I also considered generating additional data records using these examples and utilizing the GPT-3.5 model to create more examples. This approach would aid in better fine-tuning, as refining with only 60 examples may not be sufficient.