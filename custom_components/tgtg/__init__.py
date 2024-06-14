"""The TGTG integration."""
import logging

from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

from .const import DOMAIN, CONF_SECONDS, CONF_ENABLED

_LOGGER = logging.getLogger(__name__)

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the TGTG component."""

    async def handle_set_interval(service_call):
        """Handle the service call to set the update interval."""
        seconds = service_call.data.get(CONF_SECONDS, 600)
        hass.data[DOMAIN]["update_interval"] = seconds
        _LOGGER.info(f"Update interval set to {seconds} seconds")

    async def handle_enable_updates(service_call):
        """Handle the service call to enable or disable updates."""
        enabled = service_call.data.get(CONF_ENABLED, True)
        hass.data[DOMAIN]["update_enabled"] = enabled
        _LOGGER.info(f"Updates enabled: {enabled}")

    hass.services.async_register(DOMAIN, "set_interval", handle_set_interval)
    hass.services.async_register(DOMAIN, "enable_updates", handle_enable_updates)

    # Store default values for update settings
    hass.data[DOMAIN] = {
        "update_interval": 600,  # default 10 minutes
        "update_enabled": True
    }

    return True
