# Contributing to Python API Client for Digital.ai Release

## Important: Java Naming Conventions for API Classes

When adding methods to API classes (e.g., `FolderApi`, `ReleaseApi`, `PhaseApi`), **you MUST preserve Java naming
conventions**. This is critical for backwards compatibility with existing Jython scripts that depend on this library.

### Why Java Naming Conventions?

This Python library is used by Jython scripts (Python 2 running on the JVM) that were originally developed against Java
clients. To maintain compatibility, the API method signatures must match the original Java implementations exactly.

### Guidelines

1. **Method Names**: Use camelCase with the first letter lowercase (e.g., `getFolder`, `addFolder`, `listRoot`)
2. **Parameter Names**: Use camelCase to match Java conventions (e.g., `folderId`, `resultsPerPage`,
   `decorateWithPermissions`)
3. **Documentation**: Keep JavaDoc-style docstrings converted to Python format
4. **Return Types**: Ensure return types match the Java implementation

### Example

When implementing a Java API method like:

```java
@GET
@Path("/list")
List<Folder> listRoot(@QueryParam("page") Long page,
                      @QueryParam("resultsPerPage") Long resultPerPage,
                      @QueryParam("depth") Integer depth,
                      @QueryParam("permissions") Boolean decorateWithPermissions);
```

Implement it in Python as:

```python
def listRoot(
        self,
        page: int | None = None,
        resultsPerPage: int | None = None,
        depth: int | None = None,
        permissions: bool | None = None
) -> list[Folder]:
    """
    Returns a list of folders from the root directory.

    :param page: the page of results to return. Defaults to 0 if None
    :param resultsPerPage: the number of results per page. Defaults to 50 if None
    :param depth: the depth to search for. Defaults to 1 if None
    :param permissions: decorate folders with effective permissions. Defaults to False if None
    :return: a list of folders
    """
    # Implementation
```

### Note on Parameter Names in Docstrings

While method and parameter names must follow Java conventions for compatibility, parameter documentation in docstrings
should be clear and Pythonic. Refer to parameters by their exact Java-style names as they appear in the method
signature.

## Testing

- Add integration tests in `tests/integration/` for API methods
- Add unit tests in `tests/unit/` for business logic
- All tests should pass before submitting a pull request

## Code Style

Follow PEP 8 conventions for Python code except where Java naming conventions are required for API compatibility.

