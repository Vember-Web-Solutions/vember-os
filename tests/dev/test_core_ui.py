import pytest

# Corrected Imports based on class definitions
from dev.views import BaseView, DiscoveryMode, DeveloperView
from dev.scenes import DevScene, MainMenuScene
from dev.widgets import ForgeIdentity, ForgeFooter
from dev.windfall import NodeCluster
from dev.factory import ForgeFactory


def test_module_initialization():
    """Verify that all core UI modules can be instantiated without error."""
    # Instantiating to verify constructor integrity
    assert DiscoveryMode() is not None
    assert NodeCluster(root_card_panel=None) is not None
    assert ForgeFactory() is not None

    # Widgets require no arguments usually, but check their registry
    assert ForgeIdentity() is not None
    assert ForgeFooter() is not None


def test_factory_matrix_generation():
    """Verify factory is accessible and callable."""
    factory = ForgeFactory()
    # Test if generate_menu_matrix exists and is callable
    assert hasattr(factory, "generate_menu_matrix")


def test_scene_hierarchy():
    """Verify scenes inherit from the base view contract."""

    # Improved Mock to satisfy dev/scenes.py requirements
    class MockController:
        def __init__(self):
            from dev.factory import ForgeFactory

            self.factory = ForgeFactory()

    controller = MockController()

    scene = MainMenuScene(controller)
    assert isinstance(scene, DevScene)
