def simulate_llm_analysis(transcript, analysis_type):
    """
    Simulate LLM analysis (replace with actual LLM API call)
    """
    if analysis_type == "basic":
        return {"score": 85}
    elif analysis_type == "pro":
        return {"issues": ["Question 3: Lack of clarity", "Question 5: Incomplete answer"]}
    elif analysis_type == "advanced":
        return {
            "feedback": [
                {"question": "Tell me about yourself", "feedback": "Good introduction, but could elaborate more on achievements."},
                {"question": "Why do you want to join us?", "feedback": "Strong motivation, but could align more with company values."}
            ]
        }
    return {} 