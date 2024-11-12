export REPO_HOME=$HOME/repos/doc-builder-ansible-dcnm
export DOCS_EXAMPLES_DIR=$REPO_HOME/ut/examples
export DOCS_MAIN_DIR=$REPO_HOME/ut/docs
export DOCS_MODULES_DIR=$REPO_HOME/ut/py
export DOCS_RETURN_DIR=$REPO_HOME/ut/return
export DOCS_DOCUMENTATION_DIR=$REPO_HOME/ut/yaml

MODULES="dcnm_unit_test"

# --unit-test flag is used to load the unit test documentation
# from DOCS_MODULES_DIR instead of the ansible-dcnm repository
for MODULE in $MODULES; do
    echo "Retrieving Module: $MODULE"
    $REPO_HOME/doc_getter.py --module $MODULE --unit-test
done

# Create file with main DOCUMENATION section for each module
for MODULE in $MODULES; do
    echo "Processing DOCUMENTATION: $MODULE"
    $REPO_HOME/doc_builder.py $DOCS_DOCUMENTATION_DIR/$MODULE.yaml > $DOCS_MAIN_DIR/$MODULE.md
done

# Append the EXAMPLES section to each module's documentation
for MODULE in $MODULES; do
    echo "Processing EXAMPLES: $MODULE"
    echo "" >> $DOCS_MAIN_DIR/$MODULE.md
    echo "## Examples" >> $DOCS_MAIN_DIR/$MODULE.md
    echo "" >> $DOCS_MAIN_DIR/$MODULE.md
    echo '???+ "Details"' >> $DOCS_MAIN_DIR/$MODULE.md
    echo "" >> $DOCS_MAIN_DIR/$MODULE.md
    cat $DOCS_EXAMPLES_DIR/$MODULE.yaml >> $DOCS_MAIN_DIR/$MODULE.md
done

# Append the RETURN section (if it exists) to each module's documentation
for MODULE in $MODULES; do
    if [ ! -s $DOCS_RETURN_DIR/$MODULE.yaml ]; then
        continue;
    fi
    echo "Processing RETURN: $MODULE"
    echo "" >> $DOCS_MAIN_DIR/$MODULE.md
    echo "## Return" >> $DOCS_MAIN_DIR/$MODULE.md
    echo "" >> $DOCS_MAIN_DIR/$MODULE.md
    echo '???+ "Details"' >> $DOCS_MAIN_DIR/$MODULE.md
    echo "" >> $DOCS_MAIN_DIR/$MODULE.md
    cat $DOCS_RETURN_DIR/$MODULE.yaml >> $DOCS_MAIN_DIR/$MODULE.md
done
