from app.schemas import AssistantResponse


def ask_llm(question: str) -> AssistantResponse:
    if not question or not question.strip():
        raise ValueError("Question cannot be empty.")

    question_clean = question.lower().strip()

    if "carte d'identité" in question_clean or "carte didentité" in question_clean:
        return AssistantResponse(
            intent="demarche_administrative",
            category="etat_civil",
            answer="Pour refaire une carte d'identité, consultez le service état civil.",
            suggested_service="Carte d'identité",
            suggested_url="/etat-civil/carte-identite",
            confidence=0.93
        )

    if "horaires" in question_clean:
        return AssistantResponse(
            intent="demande_information",
            category="horaires_contact",
            answer="Les horaires de la mairie sont disponibles sur la page contact et horaires.",
            suggested_service="Accueil mairie",
            suggested_url="/mairie/horaires-contact",
            confidence=0.95
        )

    if "école" in question_clean or "ecole" in question_clean:
        return AssistantResponse(
            intent="demarche_administrative",
            category="scolarite",
            answer="Pour inscrire votre enfant à l'école, consultez la rubrique scolarité.",
            suggested_service="Inscription scolaire",
            suggested_url="/education/inscription-scolaire",
            confidence=0.91
        )

    if "voirie" in question_clean or "trou dans la rue" in question_clean:
        return AssistantResponse(
            intent="signalement",
            category="voirie",
            answer="Pour signaler un problème de voirie, contactez le service technique de la ville.",
            suggested_service="Signalement voirie",
            suggested_url="/services-techniques/voirie",
            confidence=0.89
        )

    if "permis de construire" in question_clean:
        return AssistantResponse(
            intent="demarche_administrative",
            category="urbanisme",
            answer="Les demandes de permis de construire relèvent du service urbanisme.",
            suggested_service="Permis de construire",
            suggested_url="/urbanisme/permis-construire",
            confidence=0.92
        )

    return AssistantResponse(
        intent="autre",
        category="autres",
        answer="Je n'ai pas encore assez de contexte pour répondre précisément à cette demande.",
        suggested_service="Contact mairie",
        suggested_url="/contact",
        confidence=0.35
    )