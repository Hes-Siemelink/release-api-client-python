# Contributing to Python API Client for Digital.ai Release

## Important: Java Naming Conventions for API Classes

When adding methods to API classes (e.g., `FolderApi`, `ReleaseApi`, `PhaseApi`), **you MUST preserve Java naming
conventions**. This is critical for backwards compatibility with existing Jython scripts that depend on this library.

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

## Domain Objects Return Type Requirement

When implementing endpoints on API classes, **methods MUST return domain objects, NOT plain dictionaries**. Use the
`from_response()` or `from_response_to_list()` methods to convert raw API responses to properly typed domain objects.

### Why This Matters

- **Type Safety**: Domain objects provide IDE autocomplete and static type checking
- **Data Validation**: Domain objects enforce data validation rules
- **Consistency**: All API methods should follow the same pattern for predictable behavior

### Example

**❌ INCORRECT - Returns plain dict:**

```python
def getFolder(self, folderId: str) -> dict:
    response = self.api.get(f"/api/v1/folders/{folderId}")
    return response  # Wrong! Returns dict
```

**✅ CORRECT - Returns domain object:**

```python
def getFolder(self, folderId: str) -> Folder:
    response = self.api.get(f"/api/v1/folders/{folderId}")
    return Folder.from_response(response)  # Correct! Returns Folder object
```

### For List Returns

Use `from_response_to_list()` for endpoints that return collections:

```python
def listRoot(self, page: int | None = None) -> list[Folder]:
    response = self.api.get("/api/v1/folders/list", params={"page": page})
    return Folder.from_response_to_list(response)  # Returns list[Folder]
```

