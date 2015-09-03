#
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

from oslo_serialization import jsonutils

from gnocchiclient.v1 import base


class ArchivePolicyManager(base.Manager):

    def list(self):
        """List archive policies

        """
        url = self.client._build_url("archive_policy")
        return self.client.api.get(url).json()

    def get(self, name):
        """Get an archive policy

        :param name: Name of the archive policy
        :type name: str
        """
        url = self.client._build_url("archive_policy/%s" % name)
        return self.client.api.get(url).json()

    def create(self, archive_policy):
        """Create an archive policy

        :param archive_policy: the archive policy
        :type archive_policy: dict

        """
        url = self.client._build_url("archive_policy/")
        return self.client.api.post(
            url, headers={'Content-Type': "application/json"},
            data=jsonutils.dumps(archive_policy)).json()

    def delete(self, name):
        """Delete an archive policy

        :param name: Name of the archive policy
        :type name: str
        """
        url = self.client._build_url("archive_policy/%s" % name)
        self.client.api.delete(url)