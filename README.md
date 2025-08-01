# Log Classification System

A robust system for classifying log messages using multiple classification approaches, including regex patterns, BERT embeddings, and LLM-based classification. This system is designed to handle logs from diverse sources and provide accurate classification, making it ideal for monitoring, troubleshooting, and analytics.

---

## Project Overview

The **Log Classification System** provides a flexible and scalable solution for organizing and classifying log messages. These logs could include application logs, server logs, or system logs. By breaking down the process into three distinct mechanisms, this system ensures greater adaptability and accuracy.

### Classification Methods

1. **Regex-Based Classification**:
   - The first line of defense in log classification.
   - Uses predefined regular expressions to quickly match known patterns in log messages.
   - Ideal for static, predictable log formats like `ERROR`, `WARNING`, or specific keyword matching.

2. **BERT-Based Classification**:
   - Employs **Bidirectional Encoder Representations from Transformers (BERT)** to generate semantic embeddings for log messages.
   - Log messages are classified based on their similarity to predefined message categories.
   - Effective for detecting patterns that go beyond simple text matches.
   - Handles cases where similar errors are described in slightly different textual formats (e.g., "Database error occurred" vs. "Issues with DB connection").

3. **LLM-Groq API-Based Classification**:
   - Utilizes a Large Language Model (LLM) API to classify complex log messages that neither regex nor BERT can handle effectively.
   - This layer allows context-based classification using AI, interpreting even poorly-structured or verbose logs.

---


## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/OthmaneAbder2303/log_classification_system.git
   cd log-classification-system
   ```

2. Create a Python virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate    # On Windows use: venv\Scripts\activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### 1. Running the Classification System

Start processing log messages by running the main script:

```bash 
  python main.py -i <input_file> -o <output_file>
```


- Replace `<input_file>` with the path to your log file(s).
- Replace `<output_file>` with the name or path of the file where classified logs will be saved.


### 2. Log Processing Workflow

Each log message undergoes classification in the following order:
1. **Regex Pattern Matching**: First, the system attempts to classify the message using predefined patterns.
2. **BERT Classification**: If regex fails, the system calculates embeddings and classifies the log semantically.
3. **LLM (Groq API)**: For messages that cannot be classified by either regex or BERT, the system sends a classification request to Groq's LLM API for advanced processing.


### 3. Configuration

Settings such as regex patterns, classification thresholds, and API keys are defined directly in the codebase. Adjust these parameters as needed in the appropriate sections of the implementation.

---

## Features

The **Log Classification System** offers several key features:

### **1. Supports Multiple Classification Scenarios**
   - Handles static logs with predictable patterns.
   - Processes complex log formats with subtle differences in wording.
   - Easily adaptable to new and custom log types.

### **2. Scalable and Modular**
   - The system is capable of processing large-scale logs efficiently.
   - Each classification method is modular, meaning you can enhance or replace specific components.

### **3. Detailed Classification Reports**
   - Outputs detailed classification results to a file in formats like `.csv` or `.json`.
   - Each log contains metadata on which classification method was used and confidence scores (if applicable).

### **4. Fault-Tolerant**
   - The system can gracefully handle log messages that cannot be classified by any of the methods, marking them as `unclassified` for further analysis.

---


## Contribution

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add feature-name'`.
4. Push to the branch: `git push origin feature-name`.
5. Open a Pull Request.

---

## Contact

If you have any questions or suggestions, feel free to contact us:

- **Email**: othmane232004@gmail.com

---

## Future Improvements

The following features may be included in future releases:

1. Support for additional APIs and Large Language Models (e.g. OpenAI, Hugging Face, etc.).
2. Improved UI/UX for real-time log classification with a dashboard.
3. Automatic tuning of BERT thresholds for optimal classification accuracy.
4. Integration with popular log aggregation tools like ELK Stack, Splunk, or Graylog.
5. Real-time stream processing for logs instead of batch processing.

