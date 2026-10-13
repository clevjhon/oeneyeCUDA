#!/usr/bin/env python3
import logging
from ops.charm import CharmBase
from ops.main import main
from ops.model import ActiveStatus

logger = logging.getLogger(__name__)

class AbuzeOperatorCharm(CharmBase):
    def __init__(self, *args):
        super().__init__(*args)
        self.framework.observe(self.on.install, self._on_install)
        self.framework.observe(self.on.config_changed, self._on_config_changed)

    def _on_install(self, event):
        logger.info("Installing abuze component: qs.abuze0")
        self.unit.status = ActiveStatus("Abuze component installed successfully")

    def _on_config_changed(self, event):
        self.unit.status = ActiveStatus("Abuze operator active")

if __name__ == "__main__":
    main(AbuzeOperatorCharm)
