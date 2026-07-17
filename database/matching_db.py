from database.db_config import get_connection


def save_match_result(
    candidate_id,
    job_id,
    match_percentage
):

    connection = get_connection()

    cursor = connection.cursor()

    query = """
    INSERT INTO resume_matches
    (candidate_id,job_id,match_percentage)
    VALUES (%s,%s,%s)
    """

    cursor.execute(
        query,
        (
            candidate_id,
            job_id,
            match_percentage
        )
    )

    connection.commit()

    cursor.close()
    connection.close()

    return True


def get_matches(candidate_id):

    connection = get_connection()

    cursor = connection.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT *
        FROM resume_matches
        WHERE candidate_id=%s
        ORDER BY created_at DESC
        """,
        (candidate_id,)
    )

    matches = cursor.fetchall()

    cursor.close()
    connection.close()

    return matches