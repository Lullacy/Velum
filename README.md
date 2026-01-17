> **System Description:**
> A content moderation system called "Velum" that filters social media posts.
>
> **Architecture:**
> 1.  **User (External Interactor)**: Submits a draft post via a web interface.
> 2.  **Frontend (Process)**: A simple web app that accepts user input and sends it to the API.
> 3.  **Velum API (Process)**: A Python FastAPI backend that processes the text.
> 4.  **Moderation Model (Data Store)**: A keyword-based ML model that checks for banned terms (e.g., "union", "strike").
>
> **Data Flow:**
> User -> Frontend: Submits Text    
> Frontend -> Velum API: POST /analyze
> Velum API -> Moderation Model: Check Content
> Moderation Model -> Velum API: Return Verdict
> Velum API -> Frontend: Return Result (Flagged/Safe)
>
> **Specific Threats to Analyze:**
> -   **Adversarial Evasion**: Users modifying text (e.g., "work stoppage" instead of "strike") to bypass the model.
> -   **Model Inversion**: Users probing the API to discover the hidden list of banned words.
> -   **Discrimination**: The model unfairly targeting specific groups (e.g., labor unions).