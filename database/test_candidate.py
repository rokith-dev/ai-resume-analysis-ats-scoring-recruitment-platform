from database.candidate_db import add_candidate

candidate_id = add_candidate(
    name="Rokith",
    email="rokith@gmail.com",
    phone="6381044437",
    target_role="AI Engineer"
)

print("Candidate ID:", candidate_id)