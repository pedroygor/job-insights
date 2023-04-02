from src.pre_built.sorting import sort_by


def test_sort_by_criteria():
    mock = [
        {
            "job_title": "Analista de Sistemas",
            "min_salary": "3000",
            "max_salary": "5000",
            "date_posted": "2023-01-01",
        },
        {
            "job_title": "Desenvolvedor Python",
            "min_salary": "4000",
            "max_salary": "6000",
            "date_posted": "2023-01-02",
        },
        {
            "job_title": "Desenvolvedor Java",
            "min_salary": "4000",
            "max_salary": "6000",
            "date_posted": "2023-01-03",
        },
        {
            "job_title": "Desenvolvedor Javascript",
            "min_salary": "4000",
            "max_salary": "6000",
            "date_posted": "2023-01-04",
        },
    ]

    sort_by(mock, "min_salary")

    assert mock[0]["job_title"] == "Analista de Sistemas"
    assert mock[1]["job_title"] == "Desenvolvedor Python"
    assert mock[2]["job_title"] == "Desenvolvedor Java"

    sort_by(mock, "max_salary")

    assert mock[0]["job_title"] == "Desenvolvedor Python"
    assert mock[1]["job_title"] == "Desenvolvedor Java"
    assert mock[2]["job_title"] == "Desenvolvedor Javascript"

    sort_by(mock, "date_posted")

    assert mock[0]["job_title"] == "Desenvolvedor Javascript"
    assert mock[1]["job_title"] == "Desenvolvedor Java"
    assert mock[2]["job_title"] == "Desenvolvedor Python"
