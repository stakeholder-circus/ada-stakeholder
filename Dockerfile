FROM ubuntu:25.10 AS build

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends gnat python3 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace
COPY src/ src/
COPY bin/ bin/
COPY tests/ tests/
RUN mkdir -p build/ada \
    && gnatmake -gnatc -D build/ada src/stakeholder_registry.ads \
    && python3 -m py_compile bin/stakeholder.py \
    && tests/test_cli.sh

FROM python:3.13-slim AS runtime
WORKDIR /app
RUN useradd --create-home --uid 10001 stakeholder
COPY --from=build --chown=stakeholder:stakeholder /workspace/bin/ ./bin/
USER stakeholder
ENTRYPOINT ["python3", "bin/stakeholder.py"]
