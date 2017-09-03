# -*- coding: utf-8 -*-

import boto3
import os
import sys
import json

"""Main module."""


class AwsHelper(object):

    _clients = []
    _default_region = 'us-west-2'

    @staticmethod
    def client(service):
        pass

    def parse_region(self, region_in=None):

        if not region_in:
            if os.environ.get("AWS_DEFAULT_REGION") is not None:
                return os.environ.get("AWS_DEFAULT_REGION")
            else:
                return AwsHelper._default_region

        return region_in


class CliHelper(object):

    @staticmethod
    def ask(prompt):
        ans = raw_input(prompt)
        return ans
