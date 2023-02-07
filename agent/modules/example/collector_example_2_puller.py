import logging
from datetime import datetime

import time

# noinspection PyUnresolvedReferences
from agent.modules.example.collector_example_2_puller_setup import CollectorExample2PullerSetup
from agent.modules.example.exceptions.exceptions import ExampleException
from devocollectorsdk.inputs.collector_puller_abstract import CollectorPullerAbstract

log = logging.getLogger(__name__)

logging.getLogger("faker.factory").setLevel(logging.WARNING)


class CollectorExample2Puller(CollectorPullerAbstract):

    FORMAT_VERSION = 1

    # def create_setup_instance(
    #         self,
    #         setup_class_name: str,
    #         autosetup_enabled: bool,
    #         collector_variables: dict) -> CollectorPullerSetupAbstract:
    #     """
    #
    #     :param setup_class_name:
    #     :param autosetup_enabled:
    #     :param collector_variables:
    #     :return:
    #     """
    #
    #     setup_class = globals()[setup_class_name]
    #     return setup_class(
    #         self,
    #         collector_variables,
    #         autosetup_enabled,
    #         self.input_id,
    #         self.input_name,
    #         self.input_config,
    #         self.input_definition,
    #         self.service_name,
    #         self.service_type,
    #         self.service_config,
    #         self.service_definition,
    #         self.module_name,
    #         self.module_config,
    #         self.module_definition,
    #         self.persistence_object,
    #         self.output_queue,
    #         self.submodule_name,
    #         self.submodule_config
    #     )

    def init_variables(
            self,
            input_config: dict,
            input_definition: dict,
            service_config: dict,
            service_definition: dict,
            module_config: dict,
            module_definition: dict,
            submodule_config: dict):
        """

        :param input_config:
        :param input_definition:
        :param service_config:
        :param service_definition:
        :param module_config:
        :param module_definition:
        :param submodule_config:
        :return:
        """

        self.log_debug(f'{self.name} Starting the execution of init_variables()')

        # Initialization of properties from credentials section from configuration
        credentials_section = input_config.get("credentials")
        if credentials_section is None:
            raise ExampleException(
                3,
                "Missing required \"credentials\" section in the configuration"
            )

        username = credentials_section.get("username")
        if username is None:
            raise ExampleException(
                0,
                "Missing required \"username\" property from \"credentials\" section in configuration"
            )
        self.collector_variables["username"] = username

        password = credentials_section.get("password")
        if password is None:
            raise ExampleException(
                1,
                "Missing required \"password\" property from \"credentials\" section in configuration"
            )
        self.collector_variables["password"] = password

        self.log_debug(f'{self.name} Finalizing the execution of init_variables()')

    def pre_pull(self, retrieving_timestamp: datetime):
        """Not required for this collector

        :param retrieving_timestamp:
        :return:
        """
        pass

    def pull(self, retrieving_timestamp: datetime):
        """

        :param retrieving_timestamp:
        :return:
        """

        self.log_debug('Starting pull()')

        example_tag = "my.app.if_framework.example_2"
        example_content = "Example text from \"example_2\""

        self.send_standard_message(datetime.utcnow(), example_tag, example_content)
        time.sleep(1)
        self.send_standard_message(datetime.utcnow(), example_tag, example_content)

        self.log_debug('Messages sent to output')

        self.log_debug('Finalizing pull()')

    def pull_stop(self) -> None:
        """Not required for this collector"""
        pass

    def pull_pause(self, wait: bool = None) -> None:
        """Not required for this collector"""
        pass
