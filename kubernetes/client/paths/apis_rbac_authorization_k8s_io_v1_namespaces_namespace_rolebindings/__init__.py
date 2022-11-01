# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from kubernetes.client.paths.apis_rbac_authorization_k8s_io_v1_namespaces_namespace_rolebindings import Api

from kubernetes.client.paths import PathValues

path = PathValues.APIS_RBAC_AUTHORIZATION_K8S_IO_V1_NAMESPACES_NAMESPACE_ROLEBINDINGS