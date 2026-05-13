---
# release-api-client-python-udbn
title: Migrate Release REST API to Python client
status: draft
type: epic
created_at: 2026-03-11T08:06:20Z
updated_at: 2026-03-11T08:06:20Z
---

Implement the full Digital.ai Release REST API as a Python client library, covering all v1 endpoints.

This epic tracks the migration of every Release REST API endpoint group into this project. Each child bean will cover one API area. The existing partial implementations (FolderApi, ReleaseApi, PhaseApi, TaskApi, TemplateApi) need to be completed, and new API classes need to be created for the remaining endpoint groups.

## Scope

### Existing API classes to complete
- **ReleaseApi** -- only getRelease is implemented; ~30 methods remain (see release_api_full.py)
- **FolderApi** -- mostly complete, verify against server docs
- **PhaseApi** -- mostly complete, verify against server docs
- **TaskApi** -- basic CRUD, may need additional endpoints
- **TemplateApi** -- basic CRUD, may need additional endpoints

### New API classes to create
- **VariableApi** -- CRUD for release/template variables
- **TeamApi** -- team and permission management
- **AttachmentApi** -- upload/download attachments
- **ArchiveApi** -- archived release operations
- **SearchApi** -- release search/filter endpoints (if separate from ReleaseApi)

### Supporting work
- Expand domain models (Variable, Team, Attachment, etc.)
- Add missing form/filter models (ReleasesFilters, AbortRelease, etc.)
- Integration test coverage for all new endpoints
- Documentation for all public API methods

## Constraints
- All method names must use Java camelCase (Jython 2 compatibility)
- All methods must return typed domain objects, never raw dicts
- Must follow existing patterns (ABC base, ReleaseAPIClient injection, from_response parsing)

## Status
Draft -- child beans will be created as we break down each API area.
