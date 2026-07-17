from database.db_config import get_connection


def get_dashboard_stats():

    connection = get_connection()

    cursor = connection.cursor(dictionary=True)

    stats = {}

    cursor.execute(
        "SELECT COUNT(*) AS total FROM candidates"
    )

    stats["total_candidates"] = cursor.fetchone()["total"]

    cursor.execute(
        "SELECT COUNT(*) AS total FROM resumes"
    )

    stats["total_resumes"] = cursor.fetchone()["total"]

    cursor.execute(
        "SELECT COUNT(*) AS total FROM job_descriptions"
    )

    stats["total_jobs"] = cursor.fetchone()["total"]

    cursor.execute(
        """
        SELECT AVG(ats_score) AS avg_score
        FROM ats_results
        """
    )

    result = cursor.fetchone()

    if result["avg_score"]:

        stats["average_ats"] = round(
            result["avg_score"],
            2
        )

    else:

        stats["average_ats"] = 0

    cursor.close()
    connection.close()

    return stats