from database.db_config import get_connection


def add_candidate(name, email, phone, target_role):
    """
    Insert a new candidate into the database.
    Returns the newly created candidate_id.
    """

    connection = get_connection()

    if connection is None:
        return None

    cursor = connection.cursor()

    query = """
    INSERT INTO candidates
    (name, email, phone, target_role)
    VALUES (%s, %s, %s, %s)
    """

    values = (
        name,
        email,
        phone,
        target_role
    )

    cursor.execute(query, values)

    connection.commit()

    candidate_id = cursor.lastrowid

    cursor.close()
    connection.close()

    return candidate_id


def get_candidate(candidate_id):
    """
    Fetch a candidate using candidate_id.
    """

    connection = get_connection()

    cursor = connection.cursor(dictionary=True)

    query = """
    SELECT *
    FROM candidates
    WHERE candidate_id = %s
    """

    cursor.execute(query, (candidate_id,))

    result = cursor.fetchone()

    cursor.close()
    connection.close()

    return result


def get_all_candidates():
    """
    Fetch all candidates.
    """

    connection = get_connection()

    cursor = connection.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT *
        FROM candidates
        ORDER BY created_at DESC
        """
    )

    results = cursor.fetchall()

    cursor.close()
    connection.close()

    return results