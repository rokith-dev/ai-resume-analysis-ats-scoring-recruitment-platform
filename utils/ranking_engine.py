def rank_candidates(candidates):
    """
    Rank candidates based on overall score.

    Parameters:
        candidates (list): List of candidate dictionaries.

    Returns:
        list: Ranked candidates in descending order.
    """

    ranked_candidates = sorted(
        candidates,
        key=lambda x: x["Overall Score"],
        reverse=True
    )

    # Assign ranks
    for index, candidate in enumerate(ranked_candidates, start=1):
        candidate["Rank"] = index

    return ranked_candidates