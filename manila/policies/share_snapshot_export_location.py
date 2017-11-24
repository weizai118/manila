#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from oslo_policy import policy

from manila.policies import base


BASE_POLICY_NAME = 'share_snapshot_export_location:%s'


share_snapshot_export_location_policies = [
    policy.DocumentedRuleDefault(
        name=BASE_POLICY_NAME % 'index',
        check_str=base.RULE_DEFAULT,
        description="List export locations of a share snapshot.",
        operations=[
            {
                'method': 'GET',
                'path': '/snapshots/{snapshot_id}/export-locations/',
            }
        ]),
    policy.DocumentedRuleDefault(
        name=BASE_POLICY_NAME % 'show',
        check_str=base.RULE_DEFAULT,
        description="Get details of a specified export location of a "
                    "share snapshot.",
        operations=[
            {
                'method': 'GET',
                'path': ('/snapshots/{snapshot_id}/'
                          'export-locations/{export_location_id}'),
            }
        ]),
]


def list_rules():
    return share_snapshot_export_location_policies
