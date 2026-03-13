def ask_llm(question: str) -> str:
    if not question or not question.strip():
        raise ValueError("Question cannot be empty.")

    question_clean = question.lower().strip()

    if "carte d'identité" in question_clean or "carte didentité" in question_clean:
        return "Pour refaire une carte d'identité, vous devez consulter le service état civil de la mairie."
    elif "horaires" in question_clean:
        return "Les horaires de la mairie sont disponibles sur la page contact et horaires."
    elif "école" in question_clean or "ecole" in question_clean:
        return "Pour inscrire votre enfant à l'école, consultez la rubrique scolarité."
    elif "voirie" in question_clean or "trou dans la rue" in question_clean:
        return "Pour signaler un problème de voirie, contactez le service technique de la ville."
    elif "permis de construire" in question_clean:
        return "Les demandes de permis de construire relèvent du service urbanisme."
    else:
        return "Je n'ai pas encore assez de contexte pour répondre précisément à cette demande."