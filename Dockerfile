# Docker validation is deferred in the M1-safe local pass.
FROM python:3.13-slim AS runtime
WORKDIR /app
COPY bin ./bin
ENTRYPOINT ["python3", "bin/stakeholder.py"]
