# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.25
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from kubernetes.client import schemas  # noqa: F401


class V1Volume(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Volume represents a named volume in a pod that may be accessed by any container in the pod.
    """


    class MetaOapg:
        required = {
            "name",
        }
        
        class properties:
            name = schemas.StrSchema
        
            @staticmethod
            def awsElasticBlockStore() -> typing.Type['V1AWSElasticBlockStoreVolumeSource']:
                return V1AWSElasticBlockStoreVolumeSource
        
            @staticmethod
            def azureDisk() -> typing.Type['V1AzureDiskVolumeSource']:
                return V1AzureDiskVolumeSource
        
            @staticmethod
            def azureFile() -> typing.Type['V1AzureFileVolumeSource']:
                return V1AzureFileVolumeSource
        
            @staticmethod
            def cephfs() -> typing.Type['V1CephFSVolumeSource']:
                return V1CephFSVolumeSource
        
            @staticmethod
            def cinder() -> typing.Type['V1CinderVolumeSource']:
                return V1CinderVolumeSource
        
            @staticmethod
            def configMap() -> typing.Type['V1ConfigMapVolumeSource']:
                return V1ConfigMapVolumeSource
        
            @staticmethod
            def csi() -> typing.Type['V1CSIVolumeSource']:
                return V1CSIVolumeSource
        
            @staticmethod
            def downwardAPI() -> typing.Type['V1DownwardAPIVolumeSource']:
                return V1DownwardAPIVolumeSource
        
            @staticmethod
            def emptyDir() -> typing.Type['V1EmptyDirVolumeSource']:
                return V1EmptyDirVolumeSource
        
            @staticmethod
            def ephemeral() -> typing.Type['V1EphemeralVolumeSource']:
                return V1EphemeralVolumeSource
        
            @staticmethod
            def fc() -> typing.Type['V1FCVolumeSource']:
                return V1FCVolumeSource
        
            @staticmethod
            def flexVolume() -> typing.Type['V1FlexVolumeSource']:
                return V1FlexVolumeSource
        
            @staticmethod
            def flocker() -> typing.Type['V1FlockerVolumeSource']:
                return V1FlockerVolumeSource
        
            @staticmethod
            def gcePersistentDisk() -> typing.Type['V1GCEPersistentDiskVolumeSource']:
                return V1GCEPersistentDiskVolumeSource
        
            @staticmethod
            def gitRepo() -> typing.Type['V1GitRepoVolumeSource']:
                return V1GitRepoVolumeSource
        
            @staticmethod
            def glusterfs() -> typing.Type['V1GlusterfsVolumeSource']:
                return V1GlusterfsVolumeSource
        
            @staticmethod
            def hostPath() -> typing.Type['V1HostPathVolumeSource']:
                return V1HostPathVolumeSource
        
            @staticmethod
            def iscsi() -> typing.Type['V1ISCSIVolumeSource']:
                return V1ISCSIVolumeSource
        
            @staticmethod
            def nfs() -> typing.Type['V1NFSVolumeSource']:
                return V1NFSVolumeSource
        
            @staticmethod
            def persistentVolumeClaim() -> typing.Type['V1PersistentVolumeClaimVolumeSource']:
                return V1PersistentVolumeClaimVolumeSource
        
            @staticmethod
            def photonPersistentDisk() -> typing.Type['V1PhotonPersistentDiskVolumeSource']:
                return V1PhotonPersistentDiskVolumeSource
        
            @staticmethod
            def portworxVolume() -> typing.Type['V1PortworxVolumeSource']:
                return V1PortworxVolumeSource
        
            @staticmethod
            def projected() -> typing.Type['V1ProjectedVolumeSource']:
                return V1ProjectedVolumeSource
        
            @staticmethod
            def quobyte() -> typing.Type['V1QuobyteVolumeSource']:
                return V1QuobyteVolumeSource
        
            @staticmethod
            def rbd() -> typing.Type['V1RBDVolumeSource']:
                return V1RBDVolumeSource
        
            @staticmethod
            def scaleIO() -> typing.Type['V1ScaleIOVolumeSource']:
                return V1ScaleIOVolumeSource
        
            @staticmethod
            def secret() -> typing.Type['V1SecretVolumeSource']:
                return V1SecretVolumeSource
        
            @staticmethod
            def storageos() -> typing.Type['V1StorageOSVolumeSource']:
                return V1StorageOSVolumeSource
        
            @staticmethod
            def vsphereVolume() -> typing.Type['V1VsphereVirtualDiskVolumeSource']:
                return V1VsphereVirtualDiskVolumeSource
            __annotations__ = {
                "name": name,
                "awsElasticBlockStore": awsElasticBlockStore,
                "azureDisk": azureDisk,
                "azureFile": azureFile,
                "cephfs": cephfs,
                "cinder": cinder,
                "configMap": configMap,
                "csi": csi,
                "downwardAPI": downwardAPI,
                "emptyDir": emptyDir,
                "ephemeral": ephemeral,
                "fc": fc,
                "flexVolume": flexVolume,
                "flocker": flocker,
                "gcePersistentDisk": gcePersistentDisk,
                "gitRepo": gitRepo,
                "glusterfs": glusterfs,
                "hostPath": hostPath,
                "iscsi": iscsi,
                "nfs": nfs,
                "persistentVolumeClaim": persistentVolumeClaim,
                "photonPersistentDisk": photonPersistentDisk,
                "portworxVolume": portworxVolume,
                "projected": projected,
                "quobyte": quobyte,
                "rbd": rbd,
                "scaleIO": scaleIO,
                "secret": secret,
                "storageos": storageos,
                "vsphereVolume": vsphereVolume,
            }
    
    name: MetaOapg.properties.name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["awsElasticBlockStore"]) -> 'V1AWSElasticBlockStoreVolumeSource': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["azureDisk"]) -> 'V1AzureDiskVolumeSource': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["azureFile"]) -> 'V1AzureFileVolumeSource': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cephfs"]) -> 'V1CephFSVolumeSource': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cinder"]) -> 'V1CinderVolumeSource': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["configMap"]) -> 'V1ConfigMapVolumeSource': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["csi"]) -> 'V1CSIVolumeSource': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["downwardAPI"]) -> 'V1DownwardAPIVolumeSource': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["emptyDir"]) -> 'V1EmptyDirVolumeSource': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ephemeral"]) -> 'V1EphemeralVolumeSource': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fc"]) -> 'V1FCVolumeSource': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["flexVolume"]) -> 'V1FlexVolumeSource': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["flocker"]) -> 'V1FlockerVolumeSource': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gcePersistentDisk"]) -> 'V1GCEPersistentDiskVolumeSource': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gitRepo"]) -> 'V1GitRepoVolumeSource': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["glusterfs"]) -> 'V1GlusterfsVolumeSource': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hostPath"]) -> 'V1HostPathVolumeSource': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["iscsi"]) -> 'V1ISCSIVolumeSource': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nfs"]) -> 'V1NFSVolumeSource': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["persistentVolumeClaim"]) -> 'V1PersistentVolumeClaimVolumeSource': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["photonPersistentDisk"]) -> 'V1PhotonPersistentDiskVolumeSource': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["portworxVolume"]) -> 'V1PortworxVolumeSource': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["projected"]) -> 'V1ProjectedVolumeSource': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["quobyte"]) -> 'V1QuobyteVolumeSource': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rbd"]) -> 'V1RBDVolumeSource': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scaleIO"]) -> 'V1ScaleIOVolumeSource': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["secret"]) -> 'V1SecretVolumeSource': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["storageos"]) -> 'V1StorageOSVolumeSource': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vsphereVolume"]) -> 'V1VsphereVirtualDiskVolumeSource': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "awsElasticBlockStore", "azureDisk", "azureFile", "cephfs", "cinder", "configMap", "csi", "downwardAPI", "emptyDir", "ephemeral", "fc", "flexVolume", "flocker", "gcePersistentDisk", "gitRepo", "glusterfs", "hostPath", "iscsi", "nfs", "persistentVolumeClaim", "photonPersistentDisk", "portworxVolume", "projected", "quobyte", "rbd", "scaleIO", "secret", "storageos", "vsphereVolume", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["awsElasticBlockStore"]) -> typing.Union['V1AWSElasticBlockStoreVolumeSource', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["azureDisk"]) -> typing.Union['V1AzureDiskVolumeSource', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["azureFile"]) -> typing.Union['V1AzureFileVolumeSource', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cephfs"]) -> typing.Union['V1CephFSVolumeSource', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cinder"]) -> typing.Union['V1CinderVolumeSource', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["configMap"]) -> typing.Union['V1ConfigMapVolumeSource', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["csi"]) -> typing.Union['V1CSIVolumeSource', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["downwardAPI"]) -> typing.Union['V1DownwardAPIVolumeSource', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["emptyDir"]) -> typing.Union['V1EmptyDirVolumeSource', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ephemeral"]) -> typing.Union['V1EphemeralVolumeSource', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fc"]) -> typing.Union['V1FCVolumeSource', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["flexVolume"]) -> typing.Union['V1FlexVolumeSource', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["flocker"]) -> typing.Union['V1FlockerVolumeSource', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gcePersistentDisk"]) -> typing.Union['V1GCEPersistentDiskVolumeSource', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gitRepo"]) -> typing.Union['V1GitRepoVolumeSource', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["glusterfs"]) -> typing.Union['V1GlusterfsVolumeSource', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hostPath"]) -> typing.Union['V1HostPathVolumeSource', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["iscsi"]) -> typing.Union['V1ISCSIVolumeSource', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nfs"]) -> typing.Union['V1NFSVolumeSource', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["persistentVolumeClaim"]) -> typing.Union['V1PersistentVolumeClaimVolumeSource', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["photonPersistentDisk"]) -> typing.Union['V1PhotonPersistentDiskVolumeSource', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["portworxVolume"]) -> typing.Union['V1PortworxVolumeSource', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["projected"]) -> typing.Union['V1ProjectedVolumeSource', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["quobyte"]) -> typing.Union['V1QuobyteVolumeSource', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rbd"]) -> typing.Union['V1RBDVolumeSource', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scaleIO"]) -> typing.Union['V1ScaleIOVolumeSource', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["secret"]) -> typing.Union['V1SecretVolumeSource', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["storageos"]) -> typing.Union['V1StorageOSVolumeSource', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vsphereVolume"]) -> typing.Union['V1VsphereVirtualDiskVolumeSource', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "awsElasticBlockStore", "azureDisk", "azureFile", "cephfs", "cinder", "configMap", "csi", "downwardAPI", "emptyDir", "ephemeral", "fc", "flexVolume", "flocker", "gcePersistentDisk", "gitRepo", "glusterfs", "hostPath", "iscsi", "nfs", "persistentVolumeClaim", "photonPersistentDisk", "portworxVolume", "projected", "quobyte", "rbd", "scaleIO", "secret", "storageos", "vsphereVolume", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        awsElasticBlockStore: typing.Union['V1AWSElasticBlockStoreVolumeSource', schemas.Unset] = schemas.unset,
        azureDisk: typing.Union['V1AzureDiskVolumeSource', schemas.Unset] = schemas.unset,
        azureFile: typing.Union['V1AzureFileVolumeSource', schemas.Unset] = schemas.unset,
        cephfs: typing.Union['V1CephFSVolumeSource', schemas.Unset] = schemas.unset,
        cinder: typing.Union['V1CinderVolumeSource', schemas.Unset] = schemas.unset,
        configMap: typing.Union['V1ConfigMapVolumeSource', schemas.Unset] = schemas.unset,
        csi: typing.Union['V1CSIVolumeSource', schemas.Unset] = schemas.unset,
        downwardAPI: typing.Union['V1DownwardAPIVolumeSource', schemas.Unset] = schemas.unset,
        emptyDir: typing.Union['V1EmptyDirVolumeSource', schemas.Unset] = schemas.unset,
        ephemeral: typing.Union['V1EphemeralVolumeSource', schemas.Unset] = schemas.unset,
        fc: typing.Union['V1FCVolumeSource', schemas.Unset] = schemas.unset,
        flexVolume: typing.Union['V1FlexVolumeSource', schemas.Unset] = schemas.unset,
        flocker: typing.Union['V1FlockerVolumeSource', schemas.Unset] = schemas.unset,
        gcePersistentDisk: typing.Union['V1GCEPersistentDiskVolumeSource', schemas.Unset] = schemas.unset,
        gitRepo: typing.Union['V1GitRepoVolumeSource', schemas.Unset] = schemas.unset,
        glusterfs: typing.Union['V1GlusterfsVolumeSource', schemas.Unset] = schemas.unset,
        hostPath: typing.Union['V1HostPathVolumeSource', schemas.Unset] = schemas.unset,
        iscsi: typing.Union['V1ISCSIVolumeSource', schemas.Unset] = schemas.unset,
        nfs: typing.Union['V1NFSVolumeSource', schemas.Unset] = schemas.unset,
        persistentVolumeClaim: typing.Union['V1PersistentVolumeClaimVolumeSource', schemas.Unset] = schemas.unset,
        photonPersistentDisk: typing.Union['V1PhotonPersistentDiskVolumeSource', schemas.Unset] = schemas.unset,
        portworxVolume: typing.Union['V1PortworxVolumeSource', schemas.Unset] = schemas.unset,
        projected: typing.Union['V1ProjectedVolumeSource', schemas.Unset] = schemas.unset,
        quobyte: typing.Union['V1QuobyteVolumeSource', schemas.Unset] = schemas.unset,
        rbd: typing.Union['V1RBDVolumeSource', schemas.Unset] = schemas.unset,
        scaleIO: typing.Union['V1ScaleIOVolumeSource', schemas.Unset] = schemas.unset,
        secret: typing.Union['V1SecretVolumeSource', schemas.Unset] = schemas.unset,
        storageos: typing.Union['V1StorageOSVolumeSource', schemas.Unset] = schemas.unset,
        vsphereVolume: typing.Union['V1VsphereVirtualDiskVolumeSource', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V1Volume':
        return super().__new__(
            cls,
            *args,
            name=name,
            awsElasticBlockStore=awsElasticBlockStore,
            azureDisk=azureDisk,
            azureFile=azureFile,
            cephfs=cephfs,
            cinder=cinder,
            configMap=configMap,
            csi=csi,
            downwardAPI=downwardAPI,
            emptyDir=emptyDir,
            ephemeral=ephemeral,
            fc=fc,
            flexVolume=flexVolume,
            flocker=flocker,
            gcePersistentDisk=gcePersistentDisk,
            gitRepo=gitRepo,
            glusterfs=glusterfs,
            hostPath=hostPath,
            iscsi=iscsi,
            nfs=nfs,
            persistentVolumeClaim=persistentVolumeClaim,
            photonPersistentDisk=photonPersistentDisk,
            portworxVolume=portworxVolume,
            projected=projected,
            quobyte=quobyte,
            rbd=rbd,
            scaleIO=scaleIO,
            secret=secret,
            storageos=storageos,
            vsphereVolume=vsphereVolume,
            _configuration=_configuration,
            **kwargs,
        )

from kubernetes.client.model.v1_aws_elastic_block_store_volume_source import V1AWSElasticBlockStoreVolumeSource
from kubernetes.client.model.v1_azure_disk_volume_source import V1AzureDiskVolumeSource
from kubernetes.client.model.v1_azure_file_volume_source import V1AzureFileVolumeSource
from kubernetes.client.model.v1_ceph_fs_volume_source import V1CephFSVolumeSource
from kubernetes.client.model.v1_cinder_volume_source import V1CinderVolumeSource
from kubernetes.client.model.v1_config_map_volume_source import V1ConfigMapVolumeSource
from kubernetes.client.model.v1_csi_volume_source import V1CSIVolumeSource
from kubernetes.client.model.v1_downward_api_volume_source import V1DownwardAPIVolumeSource
from kubernetes.client.model.v1_empty_dir_volume_source import V1EmptyDirVolumeSource
from kubernetes.client.model.v1_ephemeral_volume_source import V1EphemeralVolumeSource
from kubernetes.client.model.v1_fc_volume_source import V1FCVolumeSource
from kubernetes.client.model.v1_flex_volume_source import V1FlexVolumeSource
from kubernetes.client.model.v1_flocker_volume_source import V1FlockerVolumeSource
from kubernetes.client.model.v1_gce_persistent_disk_volume_source import V1GCEPersistentDiskVolumeSource
from kubernetes.client.model.v1_git_repo_volume_source import V1GitRepoVolumeSource
from kubernetes.client.model.v1_glusterfs_volume_source import V1GlusterfsVolumeSource
from kubernetes.client.model.v1_host_path_volume_source import V1HostPathVolumeSource
from kubernetes.client.model.v1_iscsi_volume_source import V1ISCSIVolumeSource
from kubernetes.client.model.v1_nfs_volume_source import V1NFSVolumeSource
from kubernetes.client.model.v1_persistent_volume_claim_volume_source import V1PersistentVolumeClaimVolumeSource
from kubernetes.client.model.v1_photon_persistent_disk_volume_source import V1PhotonPersistentDiskVolumeSource
from kubernetes.client.model.v1_portworx_volume_source import V1PortworxVolumeSource
from kubernetes.client.model.v1_projected_volume_source import V1ProjectedVolumeSource
from kubernetes.client.model.v1_quobyte_volume_source import V1QuobyteVolumeSource
from kubernetes.client.model.v1_rbd_volume_source import V1RBDVolumeSource
from kubernetes.client.model.v1_scale_io_volume_source import V1ScaleIOVolumeSource
from kubernetes.client.model.v1_secret_volume_source import V1SecretVolumeSource
from kubernetes.client.model.v1_storage_os_volume_source import V1StorageOSVolumeSource
from kubernetes.client.model.v1_vsphere_virtual_disk_volume_source import V1VsphereVirtualDiskVolumeSource
