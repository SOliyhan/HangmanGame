echo Is git installed?
git --version
echo
echo Is python installed?
python --version
echo
echo Are build tools installed?
mvn --version
gradle --version
ant -version
echo
echo Environment path?
env
echo Who is running this script?
whoami
echo What is workspace location?
echo $RUNNER_WORKSPACE
