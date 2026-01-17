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

``` Mermaid
graph LR
    %% Styles
    classDef actor fill:#ffe6cc,stroke:#d79b00,stroke-width:2px;
    classDef process fill:#e1f5fe,stroke:#01579b,stroke-width:2px;
    classDef store fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef threat fill:#ffcdd2,stroke:#c62828,stroke-width:2px,stroke-dasharray: 5 5;

    %% Nodes
    User("👤 Adversary<br/>(Using Evasion Tool)"):::actor
    Frontend("🖥️ Frontend POC<br/>(Edi's UI)"):::process
    API("⚙️ Velum API<br/>(FastAPI)"):::process
    Model[("🗄️ Moderation Model<br/>(The Target)")]:::store

    %% Flows
    User -- "1. Input Bad Draft" --> Frontend
    Frontend -- "2. POST /analyze" --> API
    API -- "3. Check Content" --> Model
    Model -. "4. Return Score" .-> API
    API -. "5. Return 'Flagged' Status" .-> Frontend
    Frontend -. "6. Auto-Rewrite (if Red)" .-> User

    %% Threats (Represented as floating notes attached to the relevant areas)
    T1("⚠️ T1: Oracle Attack<br/>(Learning Boundaries)"):::threat
    T2("⚠️ T2: Automated Perturbation<br/>(The Rewrite)"):::threat
    T3("⚠️ T3: Inference Exhaustion<br/>(DoS Loop)"):::threat
    T4("⚠️ T4: False Negative<br/>(Policy Bypass)"):::threat

    %% Linking Threats to Nodes (Invisible links for positioning or direct association)
    User -.- T1
    User -.- T2
    API -.- T3
    Model -.- T4
```