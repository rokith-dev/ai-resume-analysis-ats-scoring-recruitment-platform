from database.db_config import get_connection


def add_job(job_title, company, description):

    connection = get_connection()

    cursor = connection.cursor()

    query = """
    INSERT INTO job_descriptions
    (job_title, company, description)
    VALUES (%s,%s,%s)
    """

    cursor.execute(
        query,
        (
            job_title,
            company,
            description
        )
    )

    connection.commit()

    job_id = cursor.lastrowid

    cursor.close()
    connection.close()

    return job_id


def get_jobs():

    connection = get_connection()

    cursor = connection.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT *
        FROM job_descriptions
        ORDER BY created_at DESC
        """
    )

    jobs = cursor.fetchall()

    cursor.close()
    connection.close()

    return jobs