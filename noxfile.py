import nox


@nox.session(python=['3.9'])
def tests(session):
    session.install('poetry')
    session.run('poetry', 'install')
    session.run('poetry', 'build')
    session.run('poetry', 'run', 'coverage', 'run', '-m', 'pytest', '-v')
    session.run('poetry', 'run', 'coverage', 'report')


@nox.session
def lint(session):
    session.install('poetry')
    session.run('poetry', 'install')
    session.run('poetry', 'build')
    session.run('poetry', 'run', 'flake8', 'pystable', 'tests')
