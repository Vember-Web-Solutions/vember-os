from main import VemberConfig, collect_form


def test_vember_config_summary_contains_expected_fields():
    config = VemberConfig(
        project_name="vember-os",
        environment="dev",
        docker_enabled=True,
        ui_mode="form-first",
        description="Minimal shell for rebuild",
    )

    summary = config.summary()
    assert "Project: vember-os" in summary
    assert "Environment: dev" in summary
    assert "Docker: enabled" in summary
    assert "UI mode: form-first" in summary
    assert "Description: Minimal shell for rebuild" in summary


def test_collect_form_uses_default_values(monkeypatch):
    responses = iter([
        "vember-os\n",
        "dev\n",
        "y\n",
        "form-first\n",
        "Minimal shell for rebuild\n",
    ])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(responses))

    config = collect_form()

    assert config.project_name == "vember-os"
    assert config.environment == "dev"
    assert config.docker_enabled is True
    assert config.ui_mode == "form-first"
    assert config.description == "Minimal shell for rebuild"
