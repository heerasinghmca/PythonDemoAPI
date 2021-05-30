from invoke import task


@task
def start(c):
    print("Started running automation script...")
    c.run("python -m pytest -m 'positive or negative' --reruns 0 --alluredir=allure-results")