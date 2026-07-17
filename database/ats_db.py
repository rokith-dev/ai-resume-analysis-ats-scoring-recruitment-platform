from database.db_config import get_connection


def save_ats_result(candidate_id, ats_score, missing_keywords):
    """
    Save ATS analysis result.
    """

    connection = get_connection()

    if connection is None:
        return False

    cursor = connection.cursor()

    query = """
    INSERT INTO ats_results
    (candidate_id, ats_score, missing_keywords)
    VALUES (%s, %s, %s)
    """

    cursor.execute(
        query,
        (
            candidate_id,
            ats_score,
            missing_keywords
        )
    )

    connection.commit()

    cursor.close()
    connection.close()

    return True


def get_ats_results(candidate_id):

    connection = get_connection()

    cursor = connection.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT *
        FROM ats_results
        WHERE candidate_id=%s
        ORDER BY created_at DESC
        """,
        (candidate_id,)
    )

    results = cursor.fetchall()

    cursor.close()
    connection.close()

    return results