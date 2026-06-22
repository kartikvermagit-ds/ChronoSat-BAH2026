# API Reference

## `GET /health`

Returns service health.

## `POST /upload`

Accepts multipart file uploads for `.nc` and `.h5` files.

## `GET /files`

Returns the uploaded file list.

## `POST /interpolate`

Accepts:

```json
{
  "source_files": ["scene.nc"],
  "output_format": "png"
}
```

Returns a mock interpolation result without running RIFE.

## `GET /results`

Returns stored mock interpolation results.
