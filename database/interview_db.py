from database.db_config import get_connection


def save_question(
    candidate_id,
    question,
    category
):

    connection = get_connection()

    cursor = connection.cursor()

    query = """
    INSERT INTO interview_questions
    (candidate_id,question,category)
    VALUES (%s,%s,%s)
    """

    cursor.execute(
        query,
        (
            candidate_id,
            question,
            category
        )
    )

    connection.commit()

    cursor.close()
    connection.close()

    return True


def get_questions(candidate_id):

    connection = get_connection()

    cursor = connection.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT *
        FROM interview_questions
        WHERE candidate_id=%s
        ORDER BY created_at DESC
        """,
        (candidate_id,)
    )

    questions = cursor.fetchall()

    cursor.close()
    connection.close()

    return questions