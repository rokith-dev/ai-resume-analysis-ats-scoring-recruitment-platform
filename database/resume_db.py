from database.db_config import get_connection


def save_resume(candidate_id, resume_text):
    """
    Save an AI-generated resume.
    """

    connection = get_connection()

    if connection is None:
        return False

    cursor = connection.cursor()

    query = """
    INSERT INTO resumes
    (candidate_id, resume_text)
    VALUES (%s, %s)
    """

    cursor.execute(query, (candidate_id, resume_text))

    connection.commit()

    cursor.close()
    connection.close()

    return True


def get_resume(candidate_id):
    """
    Get the latest resume for a candidate.
    """

    connection = get_connection()

    cursor = connection.cursor(dictionary=True)

    query = """
    SELECT *
    FROM resumes
    WHERE candidate_id=%s
    ORDER BY created_at DESC
    LIMIT 1
    """

    cursor.execute(query, (candidate_id,))

    result = cursor.fetchone()

    cursor.close()
    connection.close()

    return result


def get_all_resumes():
    """
    Get all resumes.
    """

    connection = get_connection()

    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT *
        FROM resumes
        ORDER BY created_at DESC
    """)

    results = cursor.fetchall()

    cursor.close()
    connection.close()

    return results