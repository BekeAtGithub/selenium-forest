class PromptTemplatesAI:  # Define a class to store AI prompt templates
    CODE_VULNERABILITY_PROMPT = (
        "You are a security analyst. Analyze the following code for security vulnerabilities: \n{code_snippet}\n"
    )  # Prompt for analyzing code vulnerabilities

    LOG_SENSITIVITY_PROMPT = (
        "You are a security expert. Identify any sensitive information in the following logs: \n{log_data}\n"
    )  # Prompt for detecting sensitive data in logs

    PIPELINE_SECURITY_PROMPT = (
        "Analyze the following DevOps pipeline configuration for security risks: \n{pipeline_config}\n"
    )  # Prompt for scanning DevOps pipeline configurations

    SECRET_EXPOSURE_PROMPT = (
        "Identify any exposed secrets (API keys, passwords, tokens) in the following text: \n{text_content}\n"
    )  # Prompt for detecting exposed secrets in text
