"""
# AWS Service Catalog Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.
"""
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from ._jsii import *

import aws_cdk.core


@jsii.implements(aws_cdk.core.IInspectable)
class CfnAcceptedPortfolioShare(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-servicecatalog.CfnAcceptedPortfolioShare",
):
    """A CloudFormation ``AWS::ServiceCatalog::AcceptedPortfolioShare``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-acceptedportfolioshare.html
    :cloudformationResource: AWS::ServiceCatalog::AcceptedPortfolioShare
    """

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        portfolio_id: builtins.str,
        accept_language: typing.Optional[builtins.str] = None,
    ) -> None:
        """Create a new ``AWS::ServiceCatalog::AcceptedPortfolioShare``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param portfolio_id: ``AWS::ServiceCatalog::AcceptedPortfolioShare.PortfolioId``.
        :param accept_language: ``AWS::ServiceCatalog::AcceptedPortfolioShare.AcceptLanguage``.
        """
        props = CfnAcceptedPortfolioShareProps(
            portfolio_id=portfolio_id, accept_language=accept_language
        )

        jsii.create(CfnAcceptedPortfolioShare, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        """(experimental) Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.

        :stability: experimental
        """
        return jsii.invoke(self, "inspect", [inspector])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="portfolioId")
    def portfolio_id(self) -> builtins.str:
        """``AWS::ServiceCatalog::AcceptedPortfolioShare.PortfolioId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-acceptedportfolioshare.html#cfn-servicecatalog-acceptedportfolioshare-portfolioid
        """
        return jsii.get(self, "portfolioId")

    @portfolio_id.setter # type: ignore
    def portfolio_id(self, value: builtins.str) -> None:
        jsii.set(self, "portfolioId", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="acceptLanguage")
    def accept_language(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::AcceptedPortfolioShare.AcceptLanguage``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-acceptedportfolioshare.html#cfn-servicecatalog-acceptedportfolioshare-acceptlanguage
        """
        return jsii.get(self, "acceptLanguage")

    @accept_language.setter # type: ignore
    def accept_language(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "acceptLanguage", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-servicecatalog.CfnAcceptedPortfolioShareProps",
    jsii_struct_bases=[],
    name_mapping={"portfolio_id": "portfolioId", "accept_language": "acceptLanguage"},
)
class CfnAcceptedPortfolioShareProps:
    def __init__(
        self,
        *,
        portfolio_id: builtins.str,
        accept_language: typing.Optional[builtins.str] = None,
    ) -> None:
        """Properties for defining a ``AWS::ServiceCatalog::AcceptedPortfolioShare``.

        :param portfolio_id: ``AWS::ServiceCatalog::AcceptedPortfolioShare.PortfolioId``.
        :param accept_language: ``AWS::ServiceCatalog::AcceptedPortfolioShare.AcceptLanguage``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-acceptedportfolioshare.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "portfolio_id": portfolio_id,
        }
        if accept_language is not None:
            self._values["accept_language"] = accept_language

    @builtins.property
    def portfolio_id(self) -> builtins.str:
        """``AWS::ServiceCatalog::AcceptedPortfolioShare.PortfolioId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-acceptedportfolioshare.html#cfn-servicecatalog-acceptedportfolioshare-portfolioid
        """
        result = self._values.get("portfolio_id")
        assert result is not None, "Required property 'portfolio_id' is missing"
        return result

    @builtins.property
    def accept_language(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::AcceptedPortfolioShare.AcceptLanguage``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-acceptedportfolioshare.html#cfn-servicecatalog-acceptedportfolioshare-acceptlanguage
        """
        result = self._values.get("accept_language")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAcceptedPortfolioShareProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnCloudFormationProduct(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-servicecatalog.CfnCloudFormationProduct",
):
    """A CloudFormation ``AWS::ServiceCatalog::CloudFormationProduct``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html
    :cloudformationResource: AWS::ServiceCatalog::CloudFormationProduct
    """

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        owner: builtins.str,
        provisioning_artifact_parameters: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnCloudFormationProduct.ProvisioningArtifactPropertiesProperty", aws_cdk.core.IResolvable]]],
        accept_language: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        distributor: typing.Optional[builtins.str] = None,
        replace_provisioning_artifacts: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        support_description: typing.Optional[builtins.str] = None,
        support_email: typing.Optional[builtins.str] = None,
        support_url: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        """Create a new ``AWS::ServiceCatalog::CloudFormationProduct``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: ``AWS::ServiceCatalog::CloudFormationProduct.Name``.
        :param owner: ``AWS::ServiceCatalog::CloudFormationProduct.Owner``.
        :param provisioning_artifact_parameters: ``AWS::ServiceCatalog::CloudFormationProduct.ProvisioningArtifactParameters``.
        :param accept_language: ``AWS::ServiceCatalog::CloudFormationProduct.AcceptLanguage``.
        :param description: ``AWS::ServiceCatalog::CloudFormationProduct.Description``.
        :param distributor: ``AWS::ServiceCatalog::CloudFormationProduct.Distributor``.
        :param replace_provisioning_artifacts: ``AWS::ServiceCatalog::CloudFormationProduct.ReplaceProvisioningArtifacts``.
        :param support_description: ``AWS::ServiceCatalog::CloudFormationProduct.SupportDescription``.
        :param support_email: ``AWS::ServiceCatalog::CloudFormationProduct.SupportEmail``.
        :param support_url: ``AWS::ServiceCatalog::CloudFormationProduct.SupportUrl``.
        :param tags: ``AWS::ServiceCatalog::CloudFormationProduct.Tags``.
        """
        props = CfnCloudFormationProductProps(
            name=name,
            owner=owner,
            provisioning_artifact_parameters=provisioning_artifact_parameters,
            accept_language=accept_language,
            description=description,
            distributor=distributor,
            replace_provisioning_artifacts=replace_provisioning_artifacts,
            support_description=support_description,
            support_email=support_email,
            support_url=support_url,
            tags=tags,
        )

        jsii.create(CfnCloudFormationProduct, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        """(experimental) Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.

        :stability: experimental
        """
        return jsii.invoke(self, "inspect", [inspector])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrProductName")
    def attr_product_name(self) -> builtins.str:
        """
        :cloudformationAttribute: ProductName
        """
        return jsii.get(self, "attrProductName")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrProvisioningArtifactIds")
    def attr_provisioning_artifact_ids(self) -> builtins.str:
        """
        :cloudformationAttribute: ProvisioningArtifactIds
        """
        return jsii.get(self, "attrProvisioningArtifactIds")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrProvisioningArtifactNames")
    def attr_provisioning_artifact_names(self) -> builtins.str:
        """
        :cloudformationAttribute: ProvisioningArtifactNames
        """
        return jsii.get(self, "attrProvisioningArtifactNames")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::ServiceCatalog::CloudFormationProduct.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-tags
        """
        return jsii.get(self, "tags")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        """``AWS::ServiceCatalog::CloudFormationProduct.Name``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-name
        """
        return jsii.get(self, "name")

    @name.setter # type: ignore
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="owner")
    def owner(self) -> builtins.str:
        """``AWS::ServiceCatalog::CloudFormationProduct.Owner``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-owner
        """
        return jsii.get(self, "owner")

    @owner.setter # type: ignore
    def owner(self, value: builtins.str) -> None:
        jsii.set(self, "owner", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="provisioningArtifactParameters")
    def provisioning_artifact_parameters(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnCloudFormationProduct.ProvisioningArtifactPropertiesProperty", aws_cdk.core.IResolvable]]]:
        """``AWS::ServiceCatalog::CloudFormationProduct.ProvisioningArtifactParameters``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-provisioningartifactparameters
        """
        return jsii.get(self, "provisioningArtifactParameters")

    @provisioning_artifact_parameters.setter # type: ignore
    def provisioning_artifact_parameters(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnCloudFormationProduct.ProvisioningArtifactPropertiesProperty", aws_cdk.core.IResolvable]]],
    ) -> None:
        jsii.set(self, "provisioningArtifactParameters", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="acceptLanguage")
    def accept_language(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::CloudFormationProduct.AcceptLanguage``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-acceptlanguage
        """
        return jsii.get(self, "acceptLanguage")

    @accept_language.setter # type: ignore
    def accept_language(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "acceptLanguage", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::CloudFormationProduct.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-description
        """
        return jsii.get(self, "description")

    @description.setter # type: ignore
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="distributor")
    def distributor(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::CloudFormationProduct.Distributor``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-distributor
        """
        return jsii.get(self, "distributor")

    @distributor.setter # type: ignore
    def distributor(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "distributor", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="replaceProvisioningArtifacts")
    def replace_provisioning_artifacts(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        """``AWS::ServiceCatalog::CloudFormationProduct.ReplaceProvisioningArtifacts``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-replaceprovisioningartifacts
        """
        return jsii.get(self, "replaceProvisioningArtifacts")

    @replace_provisioning_artifacts.setter # type: ignore
    def replace_provisioning_artifacts(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "replaceProvisioningArtifacts", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="supportDescription")
    def support_description(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::CloudFormationProduct.SupportDescription``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-supportdescription
        """
        return jsii.get(self, "supportDescription")

    @support_description.setter # type: ignore
    def support_description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "supportDescription", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="supportEmail")
    def support_email(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::CloudFormationProduct.SupportEmail``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-supportemail
        """
        return jsii.get(self, "supportEmail")

    @support_email.setter # type: ignore
    def support_email(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "supportEmail", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="supportUrl")
    def support_url(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::CloudFormationProduct.SupportUrl``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-supporturl
        """
        return jsii.get(self, "supportUrl")

    @support_url.setter # type: ignore
    def support_url(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "supportUrl", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-servicecatalog.CfnCloudFormationProduct.ProvisioningArtifactPropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "info": "info",
            "description": "description",
            "disable_template_validation": "disableTemplateValidation",
            "name": "name",
        },
    )
    class ProvisioningArtifactPropertiesProperty:
        def __init__(
            self,
            *,
            info: typing.Any,
            description: typing.Optional[builtins.str] = None,
            disable_template_validation: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param info: ``CfnCloudFormationProduct.ProvisioningArtifactPropertiesProperty.Info``.
            :param description: ``CfnCloudFormationProduct.ProvisioningArtifactPropertiesProperty.Description``.
            :param disable_template_validation: ``CfnCloudFormationProduct.ProvisioningArtifactPropertiesProperty.DisableTemplateValidation``.
            :param name: ``CfnCloudFormationProduct.ProvisioningArtifactPropertiesProperty.Name``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationproduct-provisioningartifactproperties.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "info": info,
            }
            if description is not None:
                self._values["description"] = description
            if disable_template_validation is not None:
                self._values["disable_template_validation"] = disable_template_validation
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def info(self) -> typing.Any:
            """``CfnCloudFormationProduct.ProvisioningArtifactPropertiesProperty.Info``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationproduct-provisioningartifactproperties.html#cfn-servicecatalog-cloudformationproduct-provisioningartifactproperties-info
            """
            result = self._values.get("info")
            assert result is not None, "Required property 'info' is missing"
            return result

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            """``CfnCloudFormationProduct.ProvisioningArtifactPropertiesProperty.Description``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationproduct-provisioningartifactproperties.html#cfn-servicecatalog-cloudformationproduct-provisioningartifactproperties-description
            """
            result = self._values.get("description")
            return result

        @builtins.property
        def disable_template_validation(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            """``CfnCloudFormationProduct.ProvisioningArtifactPropertiesProperty.DisableTemplateValidation``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationproduct-provisioningartifactproperties.html#cfn-servicecatalog-cloudformationproduct-provisioningartifactproperties-disabletemplatevalidation
            """
            result = self._values.get("disable_template_validation")
            return result

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            """``CfnCloudFormationProduct.ProvisioningArtifactPropertiesProperty.Name``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationproduct-provisioningartifactproperties.html#cfn-servicecatalog-cloudformationproduct-provisioningartifactproperties-name
            """
            result = self._values.get("name")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProvisioningArtifactPropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-servicecatalog.CfnCloudFormationProductProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "owner": "owner",
        "provisioning_artifact_parameters": "provisioningArtifactParameters",
        "accept_language": "acceptLanguage",
        "description": "description",
        "distributor": "distributor",
        "replace_provisioning_artifacts": "replaceProvisioningArtifacts",
        "support_description": "supportDescription",
        "support_email": "supportEmail",
        "support_url": "supportUrl",
        "tags": "tags",
    },
)
class CfnCloudFormationProductProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        owner: builtins.str,
        provisioning_artifact_parameters: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[CfnCloudFormationProduct.ProvisioningArtifactPropertiesProperty, aws_cdk.core.IResolvable]]],
        accept_language: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        distributor: typing.Optional[builtins.str] = None,
        replace_provisioning_artifacts: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        support_description: typing.Optional[builtins.str] = None,
        support_email: typing.Optional[builtins.str] = None,
        support_url: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        """Properties for defining a ``AWS::ServiceCatalog::CloudFormationProduct``.

        :param name: ``AWS::ServiceCatalog::CloudFormationProduct.Name``.
        :param owner: ``AWS::ServiceCatalog::CloudFormationProduct.Owner``.
        :param provisioning_artifact_parameters: ``AWS::ServiceCatalog::CloudFormationProduct.ProvisioningArtifactParameters``.
        :param accept_language: ``AWS::ServiceCatalog::CloudFormationProduct.AcceptLanguage``.
        :param description: ``AWS::ServiceCatalog::CloudFormationProduct.Description``.
        :param distributor: ``AWS::ServiceCatalog::CloudFormationProduct.Distributor``.
        :param replace_provisioning_artifacts: ``AWS::ServiceCatalog::CloudFormationProduct.ReplaceProvisioningArtifacts``.
        :param support_description: ``AWS::ServiceCatalog::CloudFormationProduct.SupportDescription``.
        :param support_email: ``AWS::ServiceCatalog::CloudFormationProduct.SupportEmail``.
        :param support_url: ``AWS::ServiceCatalog::CloudFormationProduct.SupportUrl``.
        :param tags: ``AWS::ServiceCatalog::CloudFormationProduct.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "owner": owner,
            "provisioning_artifact_parameters": provisioning_artifact_parameters,
        }
        if accept_language is not None:
            self._values["accept_language"] = accept_language
        if description is not None:
            self._values["description"] = description
        if distributor is not None:
            self._values["distributor"] = distributor
        if replace_provisioning_artifacts is not None:
            self._values["replace_provisioning_artifacts"] = replace_provisioning_artifacts
        if support_description is not None:
            self._values["support_description"] = support_description
        if support_email is not None:
            self._values["support_email"] = support_email
        if support_url is not None:
            self._values["support_url"] = support_url
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        """``AWS::ServiceCatalog::CloudFormationProduct.Name``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-name
        """
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return result

    @builtins.property
    def owner(self) -> builtins.str:
        """``AWS::ServiceCatalog::CloudFormationProduct.Owner``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-owner
        """
        result = self._values.get("owner")
        assert result is not None, "Required property 'owner' is missing"
        return result

    @builtins.property
    def provisioning_artifact_parameters(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[CfnCloudFormationProduct.ProvisioningArtifactPropertiesProperty, aws_cdk.core.IResolvable]]]:
        """``AWS::ServiceCatalog::CloudFormationProduct.ProvisioningArtifactParameters``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-provisioningartifactparameters
        """
        result = self._values.get("provisioning_artifact_parameters")
        assert result is not None, "Required property 'provisioning_artifact_parameters' is missing"
        return result

    @builtins.property
    def accept_language(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::CloudFormationProduct.AcceptLanguage``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-acceptlanguage
        """
        result = self._values.get("accept_language")
        return result

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::CloudFormationProduct.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-description
        """
        result = self._values.get("description")
        return result

    @builtins.property
    def distributor(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::CloudFormationProduct.Distributor``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-distributor
        """
        result = self._values.get("distributor")
        return result

    @builtins.property
    def replace_provisioning_artifacts(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        """``AWS::ServiceCatalog::CloudFormationProduct.ReplaceProvisioningArtifacts``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-replaceprovisioningartifacts
        """
        result = self._values.get("replace_provisioning_artifacts")
        return result

    @builtins.property
    def support_description(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::CloudFormationProduct.SupportDescription``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-supportdescription
        """
        result = self._values.get("support_description")
        return result

    @builtins.property
    def support_email(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::CloudFormationProduct.SupportEmail``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-supportemail
        """
        result = self._values.get("support_email")
        return result

    @builtins.property
    def support_url(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::CloudFormationProduct.SupportUrl``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-supporturl
        """
        result = self._values.get("support_url")
        return result

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        """``AWS::ServiceCatalog::CloudFormationProduct.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-tags
        """
        result = self._values.get("tags")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudFormationProductProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnCloudFormationProvisionedProduct(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-servicecatalog.CfnCloudFormationProvisionedProduct",
):
    """A CloudFormation ``AWS::ServiceCatalog::CloudFormationProvisionedProduct``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html
    :cloudformationResource: AWS::ServiceCatalog::CloudFormationProvisionedProduct
    """

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        accept_language: typing.Optional[builtins.str] = None,
        notification_arns: typing.Optional[typing.List[builtins.str]] = None,
        path_id: typing.Optional[builtins.str] = None,
        path_name: typing.Optional[builtins.str] = None,
        product_id: typing.Optional[builtins.str] = None,
        product_name: typing.Optional[builtins.str] = None,
        provisioned_product_name: typing.Optional[builtins.str] = None,
        provisioning_artifact_id: typing.Optional[builtins.str] = None,
        provisioning_artifact_name: typing.Optional[builtins.str] = None,
        provisioning_parameters: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnCloudFormationProvisionedProduct.ProvisioningParameterProperty"]]]] = None,
        provisioning_preferences: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCloudFormationProvisionedProduct.ProvisioningPreferencesProperty"]] = None,
        tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        """Create a new ``AWS::ServiceCatalog::CloudFormationProvisionedProduct``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param accept_language: ``AWS::ServiceCatalog::CloudFormationProvisionedProduct.AcceptLanguage``.
        :param notification_arns: ``AWS::ServiceCatalog::CloudFormationProvisionedProduct.NotificationArns``.
        :param path_id: ``AWS::ServiceCatalog::CloudFormationProvisionedProduct.PathId``.
        :param path_name: ``AWS::ServiceCatalog::CloudFormationProvisionedProduct.PathName``.
        :param product_id: ``AWS::ServiceCatalog::CloudFormationProvisionedProduct.ProductId``.
        :param product_name: ``AWS::ServiceCatalog::CloudFormationProvisionedProduct.ProductName``.
        :param provisioned_product_name: ``AWS::ServiceCatalog::CloudFormationProvisionedProduct.ProvisionedProductName``.
        :param provisioning_artifact_id: ``AWS::ServiceCatalog::CloudFormationProvisionedProduct.ProvisioningArtifactId``.
        :param provisioning_artifact_name: ``AWS::ServiceCatalog::CloudFormationProvisionedProduct.ProvisioningArtifactName``.
        :param provisioning_parameters: ``AWS::ServiceCatalog::CloudFormationProvisionedProduct.ProvisioningParameters``.
        :param provisioning_preferences: ``AWS::ServiceCatalog::CloudFormationProvisionedProduct.ProvisioningPreferences``.
        :param tags: ``AWS::ServiceCatalog::CloudFormationProvisionedProduct.Tags``.
        """
        props = CfnCloudFormationProvisionedProductProps(
            accept_language=accept_language,
            notification_arns=notification_arns,
            path_id=path_id,
            path_name=path_name,
            product_id=product_id,
            product_name=product_name,
            provisioned_product_name=provisioned_product_name,
            provisioning_artifact_id=provisioning_artifact_id,
            provisioning_artifact_name=provisioning_artifact_name,
            provisioning_parameters=provisioning_parameters,
            provisioning_preferences=provisioning_preferences,
            tags=tags,
        )

        jsii.create(CfnCloudFormationProvisionedProduct, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        """(experimental) Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.

        :stability: experimental
        """
        return jsii.invoke(self, "inspect", [inspector])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrCloudformationStackArn")
    def attr_cloudformation_stack_arn(self) -> builtins.str:
        """
        :cloudformationAttribute: CloudformationStackArn
        """
        return jsii.get(self, "attrCloudformationStackArn")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrOutputs")
    def attr_outputs(self) -> aws_cdk.core.IResolvable:
        """
        :cloudformationAttribute: Outputs
        """
        return jsii.get(self, "attrOutputs")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrProvisionedProductId")
    def attr_provisioned_product_id(self) -> builtins.str:
        """
        :cloudformationAttribute: ProvisionedProductId
        """
        return jsii.get(self, "attrProvisionedProductId")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrRecordId")
    def attr_record_id(self) -> builtins.str:
        """
        :cloudformationAttribute: RecordId
        """
        return jsii.get(self, "attrRecordId")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::ServiceCatalog::CloudFormationProvisionedProduct.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-tags
        """
        return jsii.get(self, "tags")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="acceptLanguage")
    def accept_language(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::CloudFormationProvisionedProduct.AcceptLanguage``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-acceptlanguage
        """
        return jsii.get(self, "acceptLanguage")

    @accept_language.setter # type: ignore
    def accept_language(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "acceptLanguage", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="notificationArns")
    def notification_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        """``AWS::ServiceCatalog::CloudFormationProvisionedProduct.NotificationArns``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-notificationarns
        """
        return jsii.get(self, "notificationArns")

    @notification_arns.setter # type: ignore
    def notification_arns(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        jsii.set(self, "notificationArns", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="pathId")
    def path_id(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::CloudFormationProvisionedProduct.PathId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-pathid
        """
        return jsii.get(self, "pathId")

    @path_id.setter # type: ignore
    def path_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "pathId", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="pathName")
    def path_name(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::CloudFormationProvisionedProduct.PathName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-pathname
        """
        return jsii.get(self, "pathName")

    @path_name.setter # type: ignore
    def path_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "pathName", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="productId")
    def product_id(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::CloudFormationProvisionedProduct.ProductId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-productid
        """
        return jsii.get(self, "productId")

    @product_id.setter # type: ignore
    def product_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "productId", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="productName")
    def product_name(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::CloudFormationProvisionedProduct.ProductName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-productname
        """
        return jsii.get(self, "productName")

    @product_name.setter # type: ignore
    def product_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "productName", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="provisionedProductName")
    def provisioned_product_name(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::CloudFormationProvisionedProduct.ProvisionedProductName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisionedproductname
        """
        return jsii.get(self, "provisionedProductName")

    @provisioned_product_name.setter # type: ignore
    def provisioned_product_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "provisionedProductName", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="provisioningArtifactId")
    def provisioning_artifact_id(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::CloudFormationProvisionedProduct.ProvisioningArtifactId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningartifactid
        """
        return jsii.get(self, "provisioningArtifactId")

    @provisioning_artifact_id.setter # type: ignore
    def provisioning_artifact_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "provisioningArtifactId", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="provisioningArtifactName")
    def provisioning_artifact_name(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::CloudFormationProvisionedProduct.ProvisioningArtifactName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningartifactname
        """
        return jsii.get(self, "provisioningArtifactName")

    @provisioning_artifact_name.setter # type: ignore
    def provisioning_artifact_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "provisioningArtifactName", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="provisioningParameters")
    def provisioning_parameters(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnCloudFormationProvisionedProduct.ProvisioningParameterProperty"]]]]:
        """``AWS::ServiceCatalog::CloudFormationProvisionedProduct.ProvisioningParameters``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningparameters
        """
        return jsii.get(self, "provisioningParameters")

    @provisioning_parameters.setter # type: ignore
    def provisioning_parameters(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnCloudFormationProvisionedProduct.ProvisioningParameterProperty"]]]],
    ) -> None:
        jsii.set(self, "provisioningParameters", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="provisioningPreferences")
    def provisioning_preferences(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCloudFormationProvisionedProduct.ProvisioningPreferencesProperty"]]:
        """``AWS::ServiceCatalog::CloudFormationProvisionedProduct.ProvisioningPreferences``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences
        """
        return jsii.get(self, "provisioningPreferences")

    @provisioning_preferences.setter # type: ignore
    def provisioning_preferences(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCloudFormationProvisionedProduct.ProvisioningPreferencesProperty"]],
    ) -> None:
        jsii.set(self, "provisioningPreferences", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-servicecatalog.CfnCloudFormationProvisionedProduct.ProvisioningParameterProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class ProvisioningParameterProperty:
        def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
            """
            :param key: ``CfnCloudFormationProvisionedProduct.ProvisioningParameterProperty.Key``.
            :param value: ``CfnCloudFormationProvisionedProduct.ProvisioningParameterProperty.Value``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningparameter.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            """``CfnCloudFormationProvisionedProduct.ProvisioningParameterProperty.Key``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningparameter.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningparameter-key
            """
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return result

        @builtins.property
        def value(self) -> builtins.str:
            """``CfnCloudFormationProvisionedProduct.ProvisioningParameterProperty.Value``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningparameter.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningparameter-value
            """
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProvisioningParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-servicecatalog.CfnCloudFormationProvisionedProduct.ProvisioningPreferencesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "stack_set_accounts": "stackSetAccounts",
            "stack_set_failure_tolerance_count": "stackSetFailureToleranceCount",
            "stack_set_failure_tolerance_percentage": "stackSetFailureTolerancePercentage",
            "stack_set_max_concurrency_count": "stackSetMaxConcurrencyCount",
            "stack_set_max_concurrency_percentage": "stackSetMaxConcurrencyPercentage",
            "stack_set_operation_type": "stackSetOperationType",
            "stack_set_regions": "stackSetRegions",
        },
    )
    class ProvisioningPreferencesProperty:
        def __init__(
            self,
            *,
            stack_set_accounts: typing.Optional[typing.List[builtins.str]] = None,
            stack_set_failure_tolerance_count: typing.Optional[jsii.Number] = None,
            stack_set_failure_tolerance_percentage: typing.Optional[jsii.Number] = None,
            stack_set_max_concurrency_count: typing.Optional[jsii.Number] = None,
            stack_set_max_concurrency_percentage: typing.Optional[jsii.Number] = None,
            stack_set_operation_type: typing.Optional[builtins.str] = None,
            stack_set_regions: typing.Optional[typing.List[builtins.str]] = None,
        ) -> None:
            """
            :param stack_set_accounts: ``CfnCloudFormationProvisionedProduct.ProvisioningPreferencesProperty.StackSetAccounts``.
            :param stack_set_failure_tolerance_count: ``CfnCloudFormationProvisionedProduct.ProvisioningPreferencesProperty.StackSetFailureToleranceCount``.
            :param stack_set_failure_tolerance_percentage: ``CfnCloudFormationProvisionedProduct.ProvisioningPreferencesProperty.StackSetFailureTolerancePercentage``.
            :param stack_set_max_concurrency_count: ``CfnCloudFormationProvisionedProduct.ProvisioningPreferencesProperty.StackSetMaxConcurrencyCount``.
            :param stack_set_max_concurrency_percentage: ``CfnCloudFormationProvisionedProduct.ProvisioningPreferencesProperty.StackSetMaxConcurrencyPercentage``.
            :param stack_set_operation_type: ``CfnCloudFormationProvisionedProduct.ProvisioningPreferencesProperty.StackSetOperationType``.
            :param stack_set_regions: ``CfnCloudFormationProvisionedProduct.ProvisioningPreferencesProperty.StackSetRegions``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if stack_set_accounts is not None:
                self._values["stack_set_accounts"] = stack_set_accounts
            if stack_set_failure_tolerance_count is not None:
                self._values["stack_set_failure_tolerance_count"] = stack_set_failure_tolerance_count
            if stack_set_failure_tolerance_percentage is not None:
                self._values["stack_set_failure_tolerance_percentage"] = stack_set_failure_tolerance_percentage
            if stack_set_max_concurrency_count is not None:
                self._values["stack_set_max_concurrency_count"] = stack_set_max_concurrency_count
            if stack_set_max_concurrency_percentage is not None:
                self._values["stack_set_max_concurrency_percentage"] = stack_set_max_concurrency_percentage
            if stack_set_operation_type is not None:
                self._values["stack_set_operation_type"] = stack_set_operation_type
            if stack_set_regions is not None:
                self._values["stack_set_regions"] = stack_set_regions

        @builtins.property
        def stack_set_accounts(self) -> typing.Optional[typing.List[builtins.str]]:
            """``CfnCloudFormationProvisionedProduct.ProvisioningPreferencesProperty.StackSetAccounts``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences-stacksetaccounts
            """
            result = self._values.get("stack_set_accounts")
            return result

        @builtins.property
        def stack_set_failure_tolerance_count(self) -> typing.Optional[jsii.Number]:
            """``CfnCloudFormationProvisionedProduct.ProvisioningPreferencesProperty.StackSetFailureToleranceCount``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences-stacksetfailuretolerancecount
            """
            result = self._values.get("stack_set_failure_tolerance_count")
            return result

        @builtins.property
        def stack_set_failure_tolerance_percentage(
            self,
        ) -> typing.Optional[jsii.Number]:
            """``CfnCloudFormationProvisionedProduct.ProvisioningPreferencesProperty.StackSetFailureTolerancePercentage``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences-stacksetfailuretolerancepercentage
            """
            result = self._values.get("stack_set_failure_tolerance_percentage")
            return result

        @builtins.property
        def stack_set_max_concurrency_count(self) -> typing.Optional[jsii.Number]:
            """``CfnCloudFormationProvisionedProduct.ProvisioningPreferencesProperty.StackSetMaxConcurrencyCount``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences-stacksetmaxconcurrencycount
            """
            result = self._values.get("stack_set_max_concurrency_count")
            return result

        @builtins.property
        def stack_set_max_concurrency_percentage(self) -> typing.Optional[jsii.Number]:
            """``CfnCloudFormationProvisionedProduct.ProvisioningPreferencesProperty.StackSetMaxConcurrencyPercentage``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences-stacksetmaxconcurrencypercentage
            """
            result = self._values.get("stack_set_max_concurrency_percentage")
            return result

        @builtins.property
        def stack_set_operation_type(self) -> typing.Optional[builtins.str]:
            """``CfnCloudFormationProvisionedProduct.ProvisioningPreferencesProperty.StackSetOperationType``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences-stacksetoperationtype
            """
            result = self._values.get("stack_set_operation_type")
            return result

        @builtins.property
        def stack_set_regions(self) -> typing.Optional[typing.List[builtins.str]]:
            """``CfnCloudFormationProvisionedProduct.ProvisioningPreferencesProperty.StackSetRegions``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences-stacksetregions
            """
            result = self._values.get("stack_set_regions")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProvisioningPreferencesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-servicecatalog.CfnCloudFormationProvisionedProductProps",
    jsii_struct_bases=[],
    name_mapping={
        "accept_language": "acceptLanguage",
        "notification_arns": "notificationArns",
        "path_id": "pathId",
        "path_name": "pathName",
        "product_id": "productId",
        "product_name": "productName",
        "provisioned_product_name": "provisionedProductName",
        "provisioning_artifact_id": "provisioningArtifactId",
        "provisioning_artifact_name": "provisioningArtifactName",
        "provisioning_parameters": "provisioningParameters",
        "provisioning_preferences": "provisioningPreferences",
        "tags": "tags",
    },
)
class CfnCloudFormationProvisionedProductProps:
    def __init__(
        self,
        *,
        accept_language: typing.Optional[builtins.str] = None,
        notification_arns: typing.Optional[typing.List[builtins.str]] = None,
        path_id: typing.Optional[builtins.str] = None,
        path_name: typing.Optional[builtins.str] = None,
        product_id: typing.Optional[builtins.str] = None,
        product_name: typing.Optional[builtins.str] = None,
        provisioned_product_name: typing.Optional[builtins.str] = None,
        provisioning_artifact_id: typing.Optional[builtins.str] = None,
        provisioning_artifact_name: typing.Optional[builtins.str] = None,
        provisioning_parameters: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnCloudFormationProvisionedProduct.ProvisioningParameterProperty]]]] = None,
        provisioning_preferences: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnCloudFormationProvisionedProduct.ProvisioningPreferencesProperty]] = None,
        tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        """Properties for defining a ``AWS::ServiceCatalog::CloudFormationProvisionedProduct``.

        :param accept_language: ``AWS::ServiceCatalog::CloudFormationProvisionedProduct.AcceptLanguage``.
        :param notification_arns: ``AWS::ServiceCatalog::CloudFormationProvisionedProduct.NotificationArns``.
        :param path_id: ``AWS::ServiceCatalog::CloudFormationProvisionedProduct.PathId``.
        :param path_name: ``AWS::ServiceCatalog::CloudFormationProvisionedProduct.PathName``.
        :param product_id: ``AWS::ServiceCatalog::CloudFormationProvisionedProduct.ProductId``.
        :param product_name: ``AWS::ServiceCatalog::CloudFormationProvisionedProduct.ProductName``.
        :param provisioned_product_name: ``AWS::ServiceCatalog::CloudFormationProvisionedProduct.ProvisionedProductName``.
        :param provisioning_artifact_id: ``AWS::ServiceCatalog::CloudFormationProvisionedProduct.ProvisioningArtifactId``.
        :param provisioning_artifact_name: ``AWS::ServiceCatalog::CloudFormationProvisionedProduct.ProvisioningArtifactName``.
        :param provisioning_parameters: ``AWS::ServiceCatalog::CloudFormationProvisionedProduct.ProvisioningParameters``.
        :param provisioning_preferences: ``AWS::ServiceCatalog::CloudFormationProvisionedProduct.ProvisioningPreferences``.
        :param tags: ``AWS::ServiceCatalog::CloudFormationProvisionedProduct.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if accept_language is not None:
            self._values["accept_language"] = accept_language
        if notification_arns is not None:
            self._values["notification_arns"] = notification_arns
        if path_id is not None:
            self._values["path_id"] = path_id
        if path_name is not None:
            self._values["path_name"] = path_name
        if product_id is not None:
            self._values["product_id"] = product_id
        if product_name is not None:
            self._values["product_name"] = product_name
        if provisioned_product_name is not None:
            self._values["provisioned_product_name"] = provisioned_product_name
        if provisioning_artifact_id is not None:
            self._values["provisioning_artifact_id"] = provisioning_artifact_id
        if provisioning_artifact_name is not None:
            self._values["provisioning_artifact_name"] = provisioning_artifact_name
        if provisioning_parameters is not None:
            self._values["provisioning_parameters"] = provisioning_parameters
        if provisioning_preferences is not None:
            self._values["provisioning_preferences"] = provisioning_preferences
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def accept_language(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::CloudFormationProvisionedProduct.AcceptLanguage``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-acceptlanguage
        """
        result = self._values.get("accept_language")
        return result

    @builtins.property
    def notification_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        """``AWS::ServiceCatalog::CloudFormationProvisionedProduct.NotificationArns``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-notificationarns
        """
        result = self._values.get("notification_arns")
        return result

    @builtins.property
    def path_id(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::CloudFormationProvisionedProduct.PathId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-pathid
        """
        result = self._values.get("path_id")
        return result

    @builtins.property
    def path_name(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::CloudFormationProvisionedProduct.PathName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-pathname
        """
        result = self._values.get("path_name")
        return result

    @builtins.property
    def product_id(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::CloudFormationProvisionedProduct.ProductId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-productid
        """
        result = self._values.get("product_id")
        return result

    @builtins.property
    def product_name(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::CloudFormationProvisionedProduct.ProductName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-productname
        """
        result = self._values.get("product_name")
        return result

    @builtins.property
    def provisioned_product_name(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::CloudFormationProvisionedProduct.ProvisionedProductName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisionedproductname
        """
        result = self._values.get("provisioned_product_name")
        return result

    @builtins.property
    def provisioning_artifact_id(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::CloudFormationProvisionedProduct.ProvisioningArtifactId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningartifactid
        """
        result = self._values.get("provisioning_artifact_id")
        return result

    @builtins.property
    def provisioning_artifact_name(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::CloudFormationProvisionedProduct.ProvisioningArtifactName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningartifactname
        """
        result = self._values.get("provisioning_artifact_name")
        return result

    @builtins.property
    def provisioning_parameters(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnCloudFormationProvisionedProduct.ProvisioningParameterProperty]]]]:
        """``AWS::ServiceCatalog::CloudFormationProvisionedProduct.ProvisioningParameters``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningparameters
        """
        result = self._values.get("provisioning_parameters")
        return result

    @builtins.property
    def provisioning_preferences(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnCloudFormationProvisionedProduct.ProvisioningPreferencesProperty]]:
        """``AWS::ServiceCatalog::CloudFormationProvisionedProduct.ProvisioningPreferences``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences
        """
        result = self._values.get("provisioning_preferences")
        return result

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        """``AWS::ServiceCatalog::CloudFormationProvisionedProduct.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-tags
        """
        result = self._values.get("tags")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudFormationProvisionedProductProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnLaunchNotificationConstraint(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-servicecatalog.CfnLaunchNotificationConstraint",
):
    """A CloudFormation ``AWS::ServiceCatalog::LaunchNotificationConstraint``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchnotificationconstraint.html
    :cloudformationResource: AWS::ServiceCatalog::LaunchNotificationConstraint
    """

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        notification_arns: typing.List[builtins.str],
        portfolio_id: builtins.str,
        product_id: builtins.str,
        accept_language: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        """Create a new ``AWS::ServiceCatalog::LaunchNotificationConstraint``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param notification_arns: ``AWS::ServiceCatalog::LaunchNotificationConstraint.NotificationArns``.
        :param portfolio_id: ``AWS::ServiceCatalog::LaunchNotificationConstraint.PortfolioId``.
        :param product_id: ``AWS::ServiceCatalog::LaunchNotificationConstraint.ProductId``.
        :param accept_language: ``AWS::ServiceCatalog::LaunchNotificationConstraint.AcceptLanguage``.
        :param description: ``AWS::ServiceCatalog::LaunchNotificationConstraint.Description``.
        """
        props = CfnLaunchNotificationConstraintProps(
            notification_arns=notification_arns,
            portfolio_id=portfolio_id,
            product_id=product_id,
            accept_language=accept_language,
            description=description,
        )

        jsii.create(CfnLaunchNotificationConstraint, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        """(experimental) Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.

        :stability: experimental
        """
        return jsii.invoke(self, "inspect", [inspector])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="notificationArns")
    def notification_arns(self) -> typing.List[builtins.str]:
        """``AWS::ServiceCatalog::LaunchNotificationConstraint.NotificationArns``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchnotificationconstraint.html#cfn-servicecatalog-launchnotificationconstraint-notificationarns
        """
        return jsii.get(self, "notificationArns")

    @notification_arns.setter # type: ignore
    def notification_arns(self, value: typing.List[builtins.str]) -> None:
        jsii.set(self, "notificationArns", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="portfolioId")
    def portfolio_id(self) -> builtins.str:
        """``AWS::ServiceCatalog::LaunchNotificationConstraint.PortfolioId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchnotificationconstraint.html#cfn-servicecatalog-launchnotificationconstraint-portfolioid
        """
        return jsii.get(self, "portfolioId")

    @portfolio_id.setter # type: ignore
    def portfolio_id(self, value: builtins.str) -> None:
        jsii.set(self, "portfolioId", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="productId")
    def product_id(self) -> builtins.str:
        """``AWS::ServiceCatalog::LaunchNotificationConstraint.ProductId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchnotificationconstraint.html#cfn-servicecatalog-launchnotificationconstraint-productid
        """
        return jsii.get(self, "productId")

    @product_id.setter # type: ignore
    def product_id(self, value: builtins.str) -> None:
        jsii.set(self, "productId", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="acceptLanguage")
    def accept_language(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::LaunchNotificationConstraint.AcceptLanguage``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchnotificationconstraint.html#cfn-servicecatalog-launchnotificationconstraint-acceptlanguage
        """
        return jsii.get(self, "acceptLanguage")

    @accept_language.setter # type: ignore
    def accept_language(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "acceptLanguage", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::LaunchNotificationConstraint.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchnotificationconstraint.html#cfn-servicecatalog-launchnotificationconstraint-description
        """
        return jsii.get(self, "description")

    @description.setter # type: ignore
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-servicecatalog.CfnLaunchNotificationConstraintProps",
    jsii_struct_bases=[],
    name_mapping={
        "notification_arns": "notificationArns",
        "portfolio_id": "portfolioId",
        "product_id": "productId",
        "accept_language": "acceptLanguage",
        "description": "description",
    },
)
class CfnLaunchNotificationConstraintProps:
    def __init__(
        self,
        *,
        notification_arns: typing.List[builtins.str],
        portfolio_id: builtins.str,
        product_id: builtins.str,
        accept_language: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        """Properties for defining a ``AWS::ServiceCatalog::LaunchNotificationConstraint``.

        :param notification_arns: ``AWS::ServiceCatalog::LaunchNotificationConstraint.NotificationArns``.
        :param portfolio_id: ``AWS::ServiceCatalog::LaunchNotificationConstraint.PortfolioId``.
        :param product_id: ``AWS::ServiceCatalog::LaunchNotificationConstraint.ProductId``.
        :param accept_language: ``AWS::ServiceCatalog::LaunchNotificationConstraint.AcceptLanguage``.
        :param description: ``AWS::ServiceCatalog::LaunchNotificationConstraint.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchnotificationconstraint.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "notification_arns": notification_arns,
            "portfolio_id": portfolio_id,
            "product_id": product_id,
        }
        if accept_language is not None:
            self._values["accept_language"] = accept_language
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def notification_arns(self) -> typing.List[builtins.str]:
        """``AWS::ServiceCatalog::LaunchNotificationConstraint.NotificationArns``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchnotificationconstraint.html#cfn-servicecatalog-launchnotificationconstraint-notificationarns
        """
        result = self._values.get("notification_arns")
        assert result is not None, "Required property 'notification_arns' is missing"
        return result

    @builtins.property
    def portfolio_id(self) -> builtins.str:
        """``AWS::ServiceCatalog::LaunchNotificationConstraint.PortfolioId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchnotificationconstraint.html#cfn-servicecatalog-launchnotificationconstraint-portfolioid
        """
        result = self._values.get("portfolio_id")
        assert result is not None, "Required property 'portfolio_id' is missing"
        return result

    @builtins.property
    def product_id(self) -> builtins.str:
        """``AWS::ServiceCatalog::LaunchNotificationConstraint.ProductId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchnotificationconstraint.html#cfn-servicecatalog-launchnotificationconstraint-productid
        """
        result = self._values.get("product_id")
        assert result is not None, "Required property 'product_id' is missing"
        return result

    @builtins.property
    def accept_language(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::LaunchNotificationConstraint.AcceptLanguage``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchnotificationconstraint.html#cfn-servicecatalog-launchnotificationconstraint-acceptlanguage
        """
        result = self._values.get("accept_language")
        return result

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::LaunchNotificationConstraint.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchnotificationconstraint.html#cfn-servicecatalog-launchnotificationconstraint-description
        """
        result = self._values.get("description")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLaunchNotificationConstraintProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnLaunchRoleConstraint(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-servicecatalog.CfnLaunchRoleConstraint",
):
    """A CloudFormation ``AWS::ServiceCatalog::LaunchRoleConstraint``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchroleconstraint.html
    :cloudformationResource: AWS::ServiceCatalog::LaunchRoleConstraint
    """

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        portfolio_id: builtins.str,
        product_id: builtins.str,
        accept_language: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        local_role_name: typing.Optional[builtins.str] = None,
        role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        """Create a new ``AWS::ServiceCatalog::LaunchRoleConstraint``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param portfolio_id: ``AWS::ServiceCatalog::LaunchRoleConstraint.PortfolioId``.
        :param product_id: ``AWS::ServiceCatalog::LaunchRoleConstraint.ProductId``.
        :param accept_language: ``AWS::ServiceCatalog::LaunchRoleConstraint.AcceptLanguage``.
        :param description: ``AWS::ServiceCatalog::LaunchRoleConstraint.Description``.
        :param local_role_name: ``AWS::ServiceCatalog::LaunchRoleConstraint.LocalRoleName``.
        :param role_arn: ``AWS::ServiceCatalog::LaunchRoleConstraint.RoleArn``.
        """
        props = CfnLaunchRoleConstraintProps(
            portfolio_id=portfolio_id,
            product_id=product_id,
            accept_language=accept_language,
            description=description,
            local_role_name=local_role_name,
            role_arn=role_arn,
        )

        jsii.create(CfnLaunchRoleConstraint, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        """(experimental) Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.

        :stability: experimental
        """
        return jsii.invoke(self, "inspect", [inspector])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="portfolioId")
    def portfolio_id(self) -> builtins.str:
        """``AWS::ServiceCatalog::LaunchRoleConstraint.PortfolioId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchroleconstraint.html#cfn-servicecatalog-launchroleconstraint-portfolioid
        """
        return jsii.get(self, "portfolioId")

    @portfolio_id.setter # type: ignore
    def portfolio_id(self, value: builtins.str) -> None:
        jsii.set(self, "portfolioId", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="productId")
    def product_id(self) -> builtins.str:
        """``AWS::ServiceCatalog::LaunchRoleConstraint.ProductId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchroleconstraint.html#cfn-servicecatalog-launchroleconstraint-productid
        """
        return jsii.get(self, "productId")

    @product_id.setter # type: ignore
    def product_id(self, value: builtins.str) -> None:
        jsii.set(self, "productId", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="acceptLanguage")
    def accept_language(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::LaunchRoleConstraint.AcceptLanguage``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchroleconstraint.html#cfn-servicecatalog-launchroleconstraint-acceptlanguage
        """
        return jsii.get(self, "acceptLanguage")

    @accept_language.setter # type: ignore
    def accept_language(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "acceptLanguage", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::LaunchRoleConstraint.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchroleconstraint.html#cfn-servicecatalog-launchroleconstraint-description
        """
        return jsii.get(self, "description")

    @description.setter # type: ignore
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="localRoleName")
    def local_role_name(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::LaunchRoleConstraint.LocalRoleName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchroleconstraint.html#cfn-servicecatalog-launchroleconstraint-localrolename
        """
        return jsii.get(self, "localRoleName")

    @local_role_name.setter # type: ignore
    def local_role_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "localRoleName", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::LaunchRoleConstraint.RoleArn``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchroleconstraint.html#cfn-servicecatalog-launchroleconstraint-rolearn
        """
        return jsii.get(self, "roleArn")

    @role_arn.setter # type: ignore
    def role_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "roleArn", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-servicecatalog.CfnLaunchRoleConstraintProps",
    jsii_struct_bases=[],
    name_mapping={
        "portfolio_id": "portfolioId",
        "product_id": "productId",
        "accept_language": "acceptLanguage",
        "description": "description",
        "local_role_name": "localRoleName",
        "role_arn": "roleArn",
    },
)
class CfnLaunchRoleConstraintProps:
    def __init__(
        self,
        *,
        portfolio_id: builtins.str,
        product_id: builtins.str,
        accept_language: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        local_role_name: typing.Optional[builtins.str] = None,
        role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        """Properties for defining a ``AWS::ServiceCatalog::LaunchRoleConstraint``.

        :param portfolio_id: ``AWS::ServiceCatalog::LaunchRoleConstraint.PortfolioId``.
        :param product_id: ``AWS::ServiceCatalog::LaunchRoleConstraint.ProductId``.
        :param accept_language: ``AWS::ServiceCatalog::LaunchRoleConstraint.AcceptLanguage``.
        :param description: ``AWS::ServiceCatalog::LaunchRoleConstraint.Description``.
        :param local_role_name: ``AWS::ServiceCatalog::LaunchRoleConstraint.LocalRoleName``.
        :param role_arn: ``AWS::ServiceCatalog::LaunchRoleConstraint.RoleArn``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchroleconstraint.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "portfolio_id": portfolio_id,
            "product_id": product_id,
        }
        if accept_language is not None:
            self._values["accept_language"] = accept_language
        if description is not None:
            self._values["description"] = description
        if local_role_name is not None:
            self._values["local_role_name"] = local_role_name
        if role_arn is not None:
            self._values["role_arn"] = role_arn

    @builtins.property
    def portfolio_id(self) -> builtins.str:
        """``AWS::ServiceCatalog::LaunchRoleConstraint.PortfolioId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchroleconstraint.html#cfn-servicecatalog-launchroleconstraint-portfolioid
        """
        result = self._values.get("portfolio_id")
        assert result is not None, "Required property 'portfolio_id' is missing"
        return result

    @builtins.property
    def product_id(self) -> builtins.str:
        """``AWS::ServiceCatalog::LaunchRoleConstraint.ProductId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchroleconstraint.html#cfn-servicecatalog-launchroleconstraint-productid
        """
        result = self._values.get("product_id")
        assert result is not None, "Required property 'product_id' is missing"
        return result

    @builtins.property
    def accept_language(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::LaunchRoleConstraint.AcceptLanguage``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchroleconstraint.html#cfn-servicecatalog-launchroleconstraint-acceptlanguage
        """
        result = self._values.get("accept_language")
        return result

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::LaunchRoleConstraint.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchroleconstraint.html#cfn-servicecatalog-launchroleconstraint-description
        """
        result = self._values.get("description")
        return result

    @builtins.property
    def local_role_name(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::LaunchRoleConstraint.LocalRoleName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchroleconstraint.html#cfn-servicecatalog-launchroleconstraint-localrolename
        """
        result = self._values.get("local_role_name")
        return result

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::LaunchRoleConstraint.RoleArn``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchroleconstraint.html#cfn-servicecatalog-launchroleconstraint-rolearn
        """
        result = self._values.get("role_arn")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLaunchRoleConstraintProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnLaunchTemplateConstraint(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-servicecatalog.CfnLaunchTemplateConstraint",
):
    """A CloudFormation ``AWS::ServiceCatalog::LaunchTemplateConstraint``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchtemplateconstraint.html
    :cloudformationResource: AWS::ServiceCatalog::LaunchTemplateConstraint
    """

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        portfolio_id: builtins.str,
        product_id: builtins.str,
        rules: builtins.str,
        accept_language: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        """Create a new ``AWS::ServiceCatalog::LaunchTemplateConstraint``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param portfolio_id: ``AWS::ServiceCatalog::LaunchTemplateConstraint.PortfolioId``.
        :param product_id: ``AWS::ServiceCatalog::LaunchTemplateConstraint.ProductId``.
        :param rules: ``AWS::ServiceCatalog::LaunchTemplateConstraint.Rules``.
        :param accept_language: ``AWS::ServiceCatalog::LaunchTemplateConstraint.AcceptLanguage``.
        :param description: ``AWS::ServiceCatalog::LaunchTemplateConstraint.Description``.
        """
        props = CfnLaunchTemplateConstraintProps(
            portfolio_id=portfolio_id,
            product_id=product_id,
            rules=rules,
            accept_language=accept_language,
            description=description,
        )

        jsii.create(CfnLaunchTemplateConstraint, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        """(experimental) Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.

        :stability: experimental
        """
        return jsii.invoke(self, "inspect", [inspector])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="portfolioId")
    def portfolio_id(self) -> builtins.str:
        """``AWS::ServiceCatalog::LaunchTemplateConstraint.PortfolioId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchtemplateconstraint.html#cfn-servicecatalog-launchtemplateconstraint-portfolioid
        """
        return jsii.get(self, "portfolioId")

    @portfolio_id.setter # type: ignore
    def portfolio_id(self, value: builtins.str) -> None:
        jsii.set(self, "portfolioId", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="productId")
    def product_id(self) -> builtins.str:
        """``AWS::ServiceCatalog::LaunchTemplateConstraint.ProductId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchtemplateconstraint.html#cfn-servicecatalog-launchtemplateconstraint-productid
        """
        return jsii.get(self, "productId")

    @product_id.setter # type: ignore
    def product_id(self, value: builtins.str) -> None:
        jsii.set(self, "productId", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="rules")
    def rules(self) -> builtins.str:
        """``AWS::ServiceCatalog::LaunchTemplateConstraint.Rules``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchtemplateconstraint.html#cfn-servicecatalog-launchtemplateconstraint-rules
        """
        return jsii.get(self, "rules")

    @rules.setter # type: ignore
    def rules(self, value: builtins.str) -> None:
        jsii.set(self, "rules", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="acceptLanguage")
    def accept_language(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::LaunchTemplateConstraint.AcceptLanguage``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchtemplateconstraint.html#cfn-servicecatalog-launchtemplateconstraint-acceptlanguage
        """
        return jsii.get(self, "acceptLanguage")

    @accept_language.setter # type: ignore
    def accept_language(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "acceptLanguage", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::LaunchTemplateConstraint.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchtemplateconstraint.html#cfn-servicecatalog-launchtemplateconstraint-description
        """
        return jsii.get(self, "description")

    @description.setter # type: ignore
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-servicecatalog.CfnLaunchTemplateConstraintProps",
    jsii_struct_bases=[],
    name_mapping={
        "portfolio_id": "portfolioId",
        "product_id": "productId",
        "rules": "rules",
        "accept_language": "acceptLanguage",
        "description": "description",
    },
)
class CfnLaunchTemplateConstraintProps:
    def __init__(
        self,
        *,
        portfolio_id: builtins.str,
        product_id: builtins.str,
        rules: builtins.str,
        accept_language: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        """Properties for defining a ``AWS::ServiceCatalog::LaunchTemplateConstraint``.

        :param portfolio_id: ``AWS::ServiceCatalog::LaunchTemplateConstraint.PortfolioId``.
        :param product_id: ``AWS::ServiceCatalog::LaunchTemplateConstraint.ProductId``.
        :param rules: ``AWS::ServiceCatalog::LaunchTemplateConstraint.Rules``.
        :param accept_language: ``AWS::ServiceCatalog::LaunchTemplateConstraint.AcceptLanguage``.
        :param description: ``AWS::ServiceCatalog::LaunchTemplateConstraint.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchtemplateconstraint.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "portfolio_id": portfolio_id,
            "product_id": product_id,
            "rules": rules,
        }
        if accept_language is not None:
            self._values["accept_language"] = accept_language
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def portfolio_id(self) -> builtins.str:
        """``AWS::ServiceCatalog::LaunchTemplateConstraint.PortfolioId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchtemplateconstraint.html#cfn-servicecatalog-launchtemplateconstraint-portfolioid
        """
        result = self._values.get("portfolio_id")
        assert result is not None, "Required property 'portfolio_id' is missing"
        return result

    @builtins.property
    def product_id(self) -> builtins.str:
        """``AWS::ServiceCatalog::LaunchTemplateConstraint.ProductId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchtemplateconstraint.html#cfn-servicecatalog-launchtemplateconstraint-productid
        """
        result = self._values.get("product_id")
        assert result is not None, "Required property 'product_id' is missing"
        return result

    @builtins.property
    def rules(self) -> builtins.str:
        """``AWS::ServiceCatalog::LaunchTemplateConstraint.Rules``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchtemplateconstraint.html#cfn-servicecatalog-launchtemplateconstraint-rules
        """
        result = self._values.get("rules")
        assert result is not None, "Required property 'rules' is missing"
        return result

    @builtins.property
    def accept_language(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::LaunchTemplateConstraint.AcceptLanguage``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchtemplateconstraint.html#cfn-servicecatalog-launchtemplateconstraint-acceptlanguage
        """
        result = self._values.get("accept_language")
        return result

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::LaunchTemplateConstraint.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchtemplateconstraint.html#cfn-servicecatalog-launchtemplateconstraint-description
        """
        result = self._values.get("description")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLaunchTemplateConstraintProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnPortfolio(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-servicecatalog.CfnPortfolio",
):
    """A CloudFormation ``AWS::ServiceCatalog::Portfolio``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolio.html
    :cloudformationResource: AWS::ServiceCatalog::Portfolio
    """

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        display_name: builtins.str,
        provider_name: builtins.str,
        accept_language: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        """Create a new ``AWS::ServiceCatalog::Portfolio``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param display_name: ``AWS::ServiceCatalog::Portfolio.DisplayName``.
        :param provider_name: ``AWS::ServiceCatalog::Portfolio.ProviderName``.
        :param accept_language: ``AWS::ServiceCatalog::Portfolio.AcceptLanguage``.
        :param description: ``AWS::ServiceCatalog::Portfolio.Description``.
        :param tags: ``AWS::ServiceCatalog::Portfolio.Tags``.
        """
        props = CfnPortfolioProps(
            display_name=display_name,
            provider_name=provider_name,
            accept_language=accept_language,
            description=description,
            tags=tags,
        )

        jsii.create(CfnPortfolio, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        """(experimental) Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.

        :stability: experimental
        """
        return jsii.invoke(self, "inspect", [inspector])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrPortfolioName")
    def attr_portfolio_name(self) -> builtins.str:
        """
        :cloudformationAttribute: PortfolioName
        """
        return jsii.get(self, "attrPortfolioName")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::ServiceCatalog::Portfolio.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolio.html#cfn-servicecatalog-portfolio-tags
        """
        return jsii.get(self, "tags")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        """``AWS::ServiceCatalog::Portfolio.DisplayName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolio.html#cfn-servicecatalog-portfolio-displayname
        """
        return jsii.get(self, "displayName")

    @display_name.setter # type: ignore
    def display_name(self, value: builtins.str) -> None:
        jsii.set(self, "displayName", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="providerName")
    def provider_name(self) -> builtins.str:
        """``AWS::ServiceCatalog::Portfolio.ProviderName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolio.html#cfn-servicecatalog-portfolio-providername
        """
        return jsii.get(self, "providerName")

    @provider_name.setter # type: ignore
    def provider_name(self, value: builtins.str) -> None:
        jsii.set(self, "providerName", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="acceptLanguage")
    def accept_language(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::Portfolio.AcceptLanguage``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolio.html#cfn-servicecatalog-portfolio-acceptlanguage
        """
        return jsii.get(self, "acceptLanguage")

    @accept_language.setter # type: ignore
    def accept_language(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "acceptLanguage", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::Portfolio.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolio.html#cfn-servicecatalog-portfolio-description
        """
        return jsii.get(self, "description")

    @description.setter # type: ignore
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)


@jsii.implements(aws_cdk.core.IInspectable)
class CfnPortfolioPrincipalAssociation(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-servicecatalog.CfnPortfolioPrincipalAssociation",
):
    """A CloudFormation ``AWS::ServiceCatalog::PortfolioPrincipalAssociation``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioprincipalassociation.html
    :cloudformationResource: AWS::ServiceCatalog::PortfolioPrincipalAssociation
    """

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        portfolio_id: builtins.str,
        principal_arn: builtins.str,
        principal_type: builtins.str,
        accept_language: typing.Optional[builtins.str] = None,
    ) -> None:
        """Create a new ``AWS::ServiceCatalog::PortfolioPrincipalAssociation``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param portfolio_id: ``AWS::ServiceCatalog::PortfolioPrincipalAssociation.PortfolioId``.
        :param principal_arn: ``AWS::ServiceCatalog::PortfolioPrincipalAssociation.PrincipalARN``.
        :param principal_type: ``AWS::ServiceCatalog::PortfolioPrincipalAssociation.PrincipalType``.
        :param accept_language: ``AWS::ServiceCatalog::PortfolioPrincipalAssociation.AcceptLanguage``.
        """
        props = CfnPortfolioPrincipalAssociationProps(
            portfolio_id=portfolio_id,
            principal_arn=principal_arn,
            principal_type=principal_type,
            accept_language=accept_language,
        )

        jsii.create(CfnPortfolioPrincipalAssociation, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        """(experimental) Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.

        :stability: experimental
        """
        return jsii.invoke(self, "inspect", [inspector])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="portfolioId")
    def portfolio_id(self) -> builtins.str:
        """``AWS::ServiceCatalog::PortfolioPrincipalAssociation.PortfolioId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioprincipalassociation.html#cfn-servicecatalog-portfolioprincipalassociation-portfolioid
        """
        return jsii.get(self, "portfolioId")

    @portfolio_id.setter # type: ignore
    def portfolio_id(self, value: builtins.str) -> None:
        jsii.set(self, "portfolioId", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="principalArn")
    def principal_arn(self) -> builtins.str:
        """``AWS::ServiceCatalog::PortfolioPrincipalAssociation.PrincipalARN``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioprincipalassociation.html#cfn-servicecatalog-portfolioprincipalassociation-principalarn
        """
        return jsii.get(self, "principalArn")

    @principal_arn.setter # type: ignore
    def principal_arn(self, value: builtins.str) -> None:
        jsii.set(self, "principalArn", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="principalType")
    def principal_type(self) -> builtins.str:
        """``AWS::ServiceCatalog::PortfolioPrincipalAssociation.PrincipalType``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioprincipalassociation.html#cfn-servicecatalog-portfolioprincipalassociation-principaltype
        """
        return jsii.get(self, "principalType")

    @principal_type.setter # type: ignore
    def principal_type(self, value: builtins.str) -> None:
        jsii.set(self, "principalType", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="acceptLanguage")
    def accept_language(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::PortfolioPrincipalAssociation.AcceptLanguage``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioprincipalassociation.html#cfn-servicecatalog-portfolioprincipalassociation-acceptlanguage
        """
        return jsii.get(self, "acceptLanguage")

    @accept_language.setter # type: ignore
    def accept_language(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "acceptLanguage", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-servicecatalog.CfnPortfolioPrincipalAssociationProps",
    jsii_struct_bases=[],
    name_mapping={
        "portfolio_id": "portfolioId",
        "principal_arn": "principalArn",
        "principal_type": "principalType",
        "accept_language": "acceptLanguage",
    },
)
class CfnPortfolioPrincipalAssociationProps:
    def __init__(
        self,
        *,
        portfolio_id: builtins.str,
        principal_arn: builtins.str,
        principal_type: builtins.str,
        accept_language: typing.Optional[builtins.str] = None,
    ) -> None:
        """Properties for defining a ``AWS::ServiceCatalog::PortfolioPrincipalAssociation``.

        :param portfolio_id: ``AWS::ServiceCatalog::PortfolioPrincipalAssociation.PortfolioId``.
        :param principal_arn: ``AWS::ServiceCatalog::PortfolioPrincipalAssociation.PrincipalARN``.
        :param principal_type: ``AWS::ServiceCatalog::PortfolioPrincipalAssociation.PrincipalType``.
        :param accept_language: ``AWS::ServiceCatalog::PortfolioPrincipalAssociation.AcceptLanguage``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioprincipalassociation.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "portfolio_id": portfolio_id,
            "principal_arn": principal_arn,
            "principal_type": principal_type,
        }
        if accept_language is not None:
            self._values["accept_language"] = accept_language

    @builtins.property
    def portfolio_id(self) -> builtins.str:
        """``AWS::ServiceCatalog::PortfolioPrincipalAssociation.PortfolioId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioprincipalassociation.html#cfn-servicecatalog-portfolioprincipalassociation-portfolioid
        """
        result = self._values.get("portfolio_id")
        assert result is not None, "Required property 'portfolio_id' is missing"
        return result

    @builtins.property
    def principal_arn(self) -> builtins.str:
        """``AWS::ServiceCatalog::PortfolioPrincipalAssociation.PrincipalARN``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioprincipalassociation.html#cfn-servicecatalog-portfolioprincipalassociation-principalarn
        """
        result = self._values.get("principal_arn")
        assert result is not None, "Required property 'principal_arn' is missing"
        return result

    @builtins.property
    def principal_type(self) -> builtins.str:
        """``AWS::ServiceCatalog::PortfolioPrincipalAssociation.PrincipalType``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioprincipalassociation.html#cfn-servicecatalog-portfolioprincipalassociation-principaltype
        """
        result = self._values.get("principal_type")
        assert result is not None, "Required property 'principal_type' is missing"
        return result

    @builtins.property
    def accept_language(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::PortfolioPrincipalAssociation.AcceptLanguage``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioprincipalassociation.html#cfn-servicecatalog-portfolioprincipalassociation-acceptlanguage
        """
        result = self._values.get("accept_language")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPortfolioPrincipalAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnPortfolioProductAssociation(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-servicecatalog.CfnPortfolioProductAssociation",
):
    """A CloudFormation ``AWS::ServiceCatalog::PortfolioProductAssociation``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioproductassociation.html
    :cloudformationResource: AWS::ServiceCatalog::PortfolioProductAssociation
    """

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        portfolio_id: builtins.str,
        product_id: builtins.str,
        accept_language: typing.Optional[builtins.str] = None,
        source_portfolio_id: typing.Optional[builtins.str] = None,
    ) -> None:
        """Create a new ``AWS::ServiceCatalog::PortfolioProductAssociation``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param portfolio_id: ``AWS::ServiceCatalog::PortfolioProductAssociation.PortfolioId``.
        :param product_id: ``AWS::ServiceCatalog::PortfolioProductAssociation.ProductId``.
        :param accept_language: ``AWS::ServiceCatalog::PortfolioProductAssociation.AcceptLanguage``.
        :param source_portfolio_id: ``AWS::ServiceCatalog::PortfolioProductAssociation.SourcePortfolioId``.
        """
        props = CfnPortfolioProductAssociationProps(
            portfolio_id=portfolio_id,
            product_id=product_id,
            accept_language=accept_language,
            source_portfolio_id=source_portfolio_id,
        )

        jsii.create(CfnPortfolioProductAssociation, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        """(experimental) Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.

        :stability: experimental
        """
        return jsii.invoke(self, "inspect", [inspector])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="portfolioId")
    def portfolio_id(self) -> builtins.str:
        """``AWS::ServiceCatalog::PortfolioProductAssociation.PortfolioId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioproductassociation.html#cfn-servicecatalog-portfolioproductassociation-portfolioid
        """
        return jsii.get(self, "portfolioId")

    @portfolio_id.setter # type: ignore
    def portfolio_id(self, value: builtins.str) -> None:
        jsii.set(self, "portfolioId", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="productId")
    def product_id(self) -> builtins.str:
        """``AWS::ServiceCatalog::PortfolioProductAssociation.ProductId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioproductassociation.html#cfn-servicecatalog-portfolioproductassociation-productid
        """
        return jsii.get(self, "productId")

    @product_id.setter # type: ignore
    def product_id(self, value: builtins.str) -> None:
        jsii.set(self, "productId", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="acceptLanguage")
    def accept_language(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::PortfolioProductAssociation.AcceptLanguage``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioproductassociation.html#cfn-servicecatalog-portfolioproductassociation-acceptlanguage
        """
        return jsii.get(self, "acceptLanguage")

    @accept_language.setter # type: ignore
    def accept_language(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "acceptLanguage", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="sourcePortfolioId")
    def source_portfolio_id(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::PortfolioProductAssociation.SourcePortfolioId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioproductassociation.html#cfn-servicecatalog-portfolioproductassociation-sourceportfolioid
        """
        return jsii.get(self, "sourcePortfolioId")

    @source_portfolio_id.setter # type: ignore
    def source_portfolio_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "sourcePortfolioId", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-servicecatalog.CfnPortfolioProductAssociationProps",
    jsii_struct_bases=[],
    name_mapping={
        "portfolio_id": "portfolioId",
        "product_id": "productId",
        "accept_language": "acceptLanguage",
        "source_portfolio_id": "sourcePortfolioId",
    },
)
class CfnPortfolioProductAssociationProps:
    def __init__(
        self,
        *,
        portfolio_id: builtins.str,
        product_id: builtins.str,
        accept_language: typing.Optional[builtins.str] = None,
        source_portfolio_id: typing.Optional[builtins.str] = None,
    ) -> None:
        """Properties for defining a ``AWS::ServiceCatalog::PortfolioProductAssociation``.

        :param portfolio_id: ``AWS::ServiceCatalog::PortfolioProductAssociation.PortfolioId``.
        :param product_id: ``AWS::ServiceCatalog::PortfolioProductAssociation.ProductId``.
        :param accept_language: ``AWS::ServiceCatalog::PortfolioProductAssociation.AcceptLanguage``.
        :param source_portfolio_id: ``AWS::ServiceCatalog::PortfolioProductAssociation.SourcePortfolioId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioproductassociation.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "portfolio_id": portfolio_id,
            "product_id": product_id,
        }
        if accept_language is not None:
            self._values["accept_language"] = accept_language
        if source_portfolio_id is not None:
            self._values["source_portfolio_id"] = source_portfolio_id

    @builtins.property
    def portfolio_id(self) -> builtins.str:
        """``AWS::ServiceCatalog::PortfolioProductAssociation.PortfolioId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioproductassociation.html#cfn-servicecatalog-portfolioproductassociation-portfolioid
        """
        result = self._values.get("portfolio_id")
        assert result is not None, "Required property 'portfolio_id' is missing"
        return result

    @builtins.property
    def product_id(self) -> builtins.str:
        """``AWS::ServiceCatalog::PortfolioProductAssociation.ProductId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioproductassociation.html#cfn-servicecatalog-portfolioproductassociation-productid
        """
        result = self._values.get("product_id")
        assert result is not None, "Required property 'product_id' is missing"
        return result

    @builtins.property
    def accept_language(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::PortfolioProductAssociation.AcceptLanguage``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioproductassociation.html#cfn-servicecatalog-portfolioproductassociation-acceptlanguage
        """
        result = self._values.get("accept_language")
        return result

    @builtins.property
    def source_portfolio_id(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::PortfolioProductAssociation.SourcePortfolioId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioproductassociation.html#cfn-servicecatalog-portfolioproductassociation-sourceportfolioid
        """
        result = self._values.get("source_portfolio_id")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPortfolioProductAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-servicecatalog.CfnPortfolioProps",
    jsii_struct_bases=[],
    name_mapping={
        "display_name": "displayName",
        "provider_name": "providerName",
        "accept_language": "acceptLanguage",
        "description": "description",
        "tags": "tags",
    },
)
class CfnPortfolioProps:
    def __init__(
        self,
        *,
        display_name: builtins.str,
        provider_name: builtins.str,
        accept_language: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        """Properties for defining a ``AWS::ServiceCatalog::Portfolio``.

        :param display_name: ``AWS::ServiceCatalog::Portfolio.DisplayName``.
        :param provider_name: ``AWS::ServiceCatalog::Portfolio.ProviderName``.
        :param accept_language: ``AWS::ServiceCatalog::Portfolio.AcceptLanguage``.
        :param description: ``AWS::ServiceCatalog::Portfolio.Description``.
        :param tags: ``AWS::ServiceCatalog::Portfolio.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolio.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "display_name": display_name,
            "provider_name": provider_name,
        }
        if accept_language is not None:
            self._values["accept_language"] = accept_language
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def display_name(self) -> builtins.str:
        """``AWS::ServiceCatalog::Portfolio.DisplayName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolio.html#cfn-servicecatalog-portfolio-displayname
        """
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return result

    @builtins.property
    def provider_name(self) -> builtins.str:
        """``AWS::ServiceCatalog::Portfolio.ProviderName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolio.html#cfn-servicecatalog-portfolio-providername
        """
        result = self._values.get("provider_name")
        assert result is not None, "Required property 'provider_name' is missing"
        return result

    @builtins.property
    def accept_language(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::Portfolio.AcceptLanguage``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolio.html#cfn-servicecatalog-portfolio-acceptlanguage
        """
        result = self._values.get("accept_language")
        return result

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::Portfolio.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolio.html#cfn-servicecatalog-portfolio-description
        """
        result = self._values.get("description")
        return result

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        """``AWS::ServiceCatalog::Portfolio.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolio.html#cfn-servicecatalog-portfolio-tags
        """
        result = self._values.get("tags")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPortfolioProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnPortfolioShare(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-servicecatalog.CfnPortfolioShare",
):
    """A CloudFormation ``AWS::ServiceCatalog::PortfolioShare``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioshare.html
    :cloudformationResource: AWS::ServiceCatalog::PortfolioShare
    """

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        account_id: builtins.str,
        portfolio_id: builtins.str,
        accept_language: typing.Optional[builtins.str] = None,
    ) -> None:
        """Create a new ``AWS::ServiceCatalog::PortfolioShare``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param account_id: ``AWS::ServiceCatalog::PortfolioShare.AccountId``.
        :param portfolio_id: ``AWS::ServiceCatalog::PortfolioShare.PortfolioId``.
        :param accept_language: ``AWS::ServiceCatalog::PortfolioShare.AcceptLanguage``.
        """
        props = CfnPortfolioShareProps(
            account_id=account_id,
            portfolio_id=portfolio_id,
            accept_language=accept_language,
        )

        jsii.create(CfnPortfolioShare, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        """(experimental) Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.

        :stability: experimental
        """
        return jsii.invoke(self, "inspect", [inspector])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> builtins.str:
        """``AWS::ServiceCatalog::PortfolioShare.AccountId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioshare.html#cfn-servicecatalog-portfolioshare-accountid
        """
        return jsii.get(self, "accountId")

    @account_id.setter # type: ignore
    def account_id(self, value: builtins.str) -> None:
        jsii.set(self, "accountId", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="portfolioId")
    def portfolio_id(self) -> builtins.str:
        """``AWS::ServiceCatalog::PortfolioShare.PortfolioId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioshare.html#cfn-servicecatalog-portfolioshare-portfolioid
        """
        return jsii.get(self, "portfolioId")

    @portfolio_id.setter # type: ignore
    def portfolio_id(self, value: builtins.str) -> None:
        jsii.set(self, "portfolioId", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="acceptLanguage")
    def accept_language(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::PortfolioShare.AcceptLanguage``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioshare.html#cfn-servicecatalog-portfolioshare-acceptlanguage
        """
        return jsii.get(self, "acceptLanguage")

    @accept_language.setter # type: ignore
    def accept_language(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "acceptLanguage", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-servicecatalog.CfnPortfolioShareProps",
    jsii_struct_bases=[],
    name_mapping={
        "account_id": "accountId",
        "portfolio_id": "portfolioId",
        "accept_language": "acceptLanguage",
    },
)
class CfnPortfolioShareProps:
    def __init__(
        self,
        *,
        account_id: builtins.str,
        portfolio_id: builtins.str,
        accept_language: typing.Optional[builtins.str] = None,
    ) -> None:
        """Properties for defining a ``AWS::ServiceCatalog::PortfolioShare``.

        :param account_id: ``AWS::ServiceCatalog::PortfolioShare.AccountId``.
        :param portfolio_id: ``AWS::ServiceCatalog::PortfolioShare.PortfolioId``.
        :param accept_language: ``AWS::ServiceCatalog::PortfolioShare.AcceptLanguage``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioshare.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "account_id": account_id,
            "portfolio_id": portfolio_id,
        }
        if accept_language is not None:
            self._values["accept_language"] = accept_language

    @builtins.property
    def account_id(self) -> builtins.str:
        """``AWS::ServiceCatalog::PortfolioShare.AccountId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioshare.html#cfn-servicecatalog-portfolioshare-accountid
        """
        result = self._values.get("account_id")
        assert result is not None, "Required property 'account_id' is missing"
        return result

    @builtins.property
    def portfolio_id(self) -> builtins.str:
        """``AWS::ServiceCatalog::PortfolioShare.PortfolioId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioshare.html#cfn-servicecatalog-portfolioshare-portfolioid
        """
        result = self._values.get("portfolio_id")
        assert result is not None, "Required property 'portfolio_id' is missing"
        return result

    @builtins.property
    def accept_language(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::PortfolioShare.AcceptLanguage``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioshare.html#cfn-servicecatalog-portfolioshare-acceptlanguage
        """
        result = self._values.get("accept_language")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPortfolioShareProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnResourceUpdateConstraint(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-servicecatalog.CfnResourceUpdateConstraint",
):
    """A CloudFormation ``AWS::ServiceCatalog::ResourceUpdateConstraint``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-resourceupdateconstraint.html
    :cloudformationResource: AWS::ServiceCatalog::ResourceUpdateConstraint
    """

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        portfolio_id: builtins.str,
        product_id: builtins.str,
        tag_update_on_provisioned_product: builtins.str,
        accept_language: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        """Create a new ``AWS::ServiceCatalog::ResourceUpdateConstraint``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param portfolio_id: ``AWS::ServiceCatalog::ResourceUpdateConstraint.PortfolioId``.
        :param product_id: ``AWS::ServiceCatalog::ResourceUpdateConstraint.ProductId``.
        :param tag_update_on_provisioned_product: ``AWS::ServiceCatalog::ResourceUpdateConstraint.TagUpdateOnProvisionedProduct``.
        :param accept_language: ``AWS::ServiceCatalog::ResourceUpdateConstraint.AcceptLanguage``.
        :param description: ``AWS::ServiceCatalog::ResourceUpdateConstraint.Description``.
        """
        props = CfnResourceUpdateConstraintProps(
            portfolio_id=portfolio_id,
            product_id=product_id,
            tag_update_on_provisioned_product=tag_update_on_provisioned_product,
            accept_language=accept_language,
            description=description,
        )

        jsii.create(CfnResourceUpdateConstraint, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        """(experimental) Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.

        :stability: experimental
        """
        return jsii.invoke(self, "inspect", [inspector])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="portfolioId")
    def portfolio_id(self) -> builtins.str:
        """``AWS::ServiceCatalog::ResourceUpdateConstraint.PortfolioId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-resourceupdateconstraint.html#cfn-servicecatalog-resourceupdateconstraint-portfolioid
        """
        return jsii.get(self, "portfolioId")

    @portfolio_id.setter # type: ignore
    def portfolio_id(self, value: builtins.str) -> None:
        jsii.set(self, "portfolioId", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="productId")
    def product_id(self) -> builtins.str:
        """``AWS::ServiceCatalog::ResourceUpdateConstraint.ProductId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-resourceupdateconstraint.html#cfn-servicecatalog-resourceupdateconstraint-productid
        """
        return jsii.get(self, "productId")

    @product_id.setter # type: ignore
    def product_id(self, value: builtins.str) -> None:
        jsii.set(self, "productId", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="tagUpdateOnProvisionedProduct")
    def tag_update_on_provisioned_product(self) -> builtins.str:
        """``AWS::ServiceCatalog::ResourceUpdateConstraint.TagUpdateOnProvisionedProduct``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-resourceupdateconstraint.html#cfn-servicecatalog-resourceupdateconstraint-tagupdateonprovisionedproduct
        """
        return jsii.get(self, "tagUpdateOnProvisionedProduct")

    @tag_update_on_provisioned_product.setter # type: ignore
    def tag_update_on_provisioned_product(self, value: builtins.str) -> None:
        jsii.set(self, "tagUpdateOnProvisionedProduct", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="acceptLanguage")
    def accept_language(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::ResourceUpdateConstraint.AcceptLanguage``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-resourceupdateconstraint.html#cfn-servicecatalog-resourceupdateconstraint-acceptlanguage
        """
        return jsii.get(self, "acceptLanguage")

    @accept_language.setter # type: ignore
    def accept_language(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "acceptLanguage", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::ResourceUpdateConstraint.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-resourceupdateconstraint.html#cfn-servicecatalog-resourceupdateconstraint-description
        """
        return jsii.get(self, "description")

    @description.setter # type: ignore
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-servicecatalog.CfnResourceUpdateConstraintProps",
    jsii_struct_bases=[],
    name_mapping={
        "portfolio_id": "portfolioId",
        "product_id": "productId",
        "tag_update_on_provisioned_product": "tagUpdateOnProvisionedProduct",
        "accept_language": "acceptLanguage",
        "description": "description",
    },
)
class CfnResourceUpdateConstraintProps:
    def __init__(
        self,
        *,
        portfolio_id: builtins.str,
        product_id: builtins.str,
        tag_update_on_provisioned_product: builtins.str,
        accept_language: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        """Properties for defining a ``AWS::ServiceCatalog::ResourceUpdateConstraint``.

        :param portfolio_id: ``AWS::ServiceCatalog::ResourceUpdateConstraint.PortfolioId``.
        :param product_id: ``AWS::ServiceCatalog::ResourceUpdateConstraint.ProductId``.
        :param tag_update_on_provisioned_product: ``AWS::ServiceCatalog::ResourceUpdateConstraint.TagUpdateOnProvisionedProduct``.
        :param accept_language: ``AWS::ServiceCatalog::ResourceUpdateConstraint.AcceptLanguage``.
        :param description: ``AWS::ServiceCatalog::ResourceUpdateConstraint.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-resourceupdateconstraint.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "portfolio_id": portfolio_id,
            "product_id": product_id,
            "tag_update_on_provisioned_product": tag_update_on_provisioned_product,
        }
        if accept_language is not None:
            self._values["accept_language"] = accept_language
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def portfolio_id(self) -> builtins.str:
        """``AWS::ServiceCatalog::ResourceUpdateConstraint.PortfolioId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-resourceupdateconstraint.html#cfn-servicecatalog-resourceupdateconstraint-portfolioid
        """
        result = self._values.get("portfolio_id")
        assert result is not None, "Required property 'portfolio_id' is missing"
        return result

    @builtins.property
    def product_id(self) -> builtins.str:
        """``AWS::ServiceCatalog::ResourceUpdateConstraint.ProductId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-resourceupdateconstraint.html#cfn-servicecatalog-resourceupdateconstraint-productid
        """
        result = self._values.get("product_id")
        assert result is not None, "Required property 'product_id' is missing"
        return result

    @builtins.property
    def tag_update_on_provisioned_product(self) -> builtins.str:
        """``AWS::ServiceCatalog::ResourceUpdateConstraint.TagUpdateOnProvisionedProduct``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-resourceupdateconstraint.html#cfn-servicecatalog-resourceupdateconstraint-tagupdateonprovisionedproduct
        """
        result = self._values.get("tag_update_on_provisioned_product")
        assert result is not None, "Required property 'tag_update_on_provisioned_product' is missing"
        return result

    @builtins.property
    def accept_language(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::ResourceUpdateConstraint.AcceptLanguage``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-resourceupdateconstraint.html#cfn-servicecatalog-resourceupdateconstraint-acceptlanguage
        """
        result = self._values.get("accept_language")
        return result

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::ResourceUpdateConstraint.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-resourceupdateconstraint.html#cfn-servicecatalog-resourceupdateconstraint-description
        """
        result = self._values.get("description")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResourceUpdateConstraintProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnStackSetConstraint(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-servicecatalog.CfnStackSetConstraint",
):
    """A CloudFormation ``AWS::ServiceCatalog::StackSetConstraint``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html
    :cloudformationResource: AWS::ServiceCatalog::StackSetConstraint
    """

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        account_list: typing.List[builtins.str],
        admin_role: builtins.str,
        description: builtins.str,
        execution_role: builtins.str,
        portfolio_id: builtins.str,
        product_id: builtins.str,
        region_list: typing.List[builtins.str],
        stack_instance_control: builtins.str,
        accept_language: typing.Optional[builtins.str] = None,
    ) -> None:
        """Create a new ``AWS::ServiceCatalog::StackSetConstraint``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param account_list: ``AWS::ServiceCatalog::StackSetConstraint.AccountList``.
        :param admin_role: ``AWS::ServiceCatalog::StackSetConstraint.AdminRole``.
        :param description: ``AWS::ServiceCatalog::StackSetConstraint.Description``.
        :param execution_role: ``AWS::ServiceCatalog::StackSetConstraint.ExecutionRole``.
        :param portfolio_id: ``AWS::ServiceCatalog::StackSetConstraint.PortfolioId``.
        :param product_id: ``AWS::ServiceCatalog::StackSetConstraint.ProductId``.
        :param region_list: ``AWS::ServiceCatalog::StackSetConstraint.RegionList``.
        :param stack_instance_control: ``AWS::ServiceCatalog::StackSetConstraint.StackInstanceControl``.
        :param accept_language: ``AWS::ServiceCatalog::StackSetConstraint.AcceptLanguage``.
        """
        props = CfnStackSetConstraintProps(
            account_list=account_list,
            admin_role=admin_role,
            description=description,
            execution_role=execution_role,
            portfolio_id=portfolio_id,
            product_id=product_id,
            region_list=region_list,
            stack_instance_control=stack_instance_control,
            accept_language=accept_language,
        )

        jsii.create(CfnStackSetConstraint, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        """(experimental) Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.

        :stability: experimental
        """
        return jsii.invoke(self, "inspect", [inspector])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="accountList")
    def account_list(self) -> typing.List[builtins.str]:
        """``AWS::ServiceCatalog::StackSetConstraint.AccountList``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-accountlist
        """
        return jsii.get(self, "accountList")

    @account_list.setter # type: ignore
    def account_list(self, value: typing.List[builtins.str]) -> None:
        jsii.set(self, "accountList", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="adminRole")
    def admin_role(self) -> builtins.str:
        """``AWS::ServiceCatalog::StackSetConstraint.AdminRole``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-adminrole
        """
        return jsii.get(self, "adminRole")

    @admin_role.setter # type: ignore
    def admin_role(self, value: builtins.str) -> None:
        jsii.set(self, "adminRole", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        """``AWS::ServiceCatalog::StackSetConstraint.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-description
        """
        return jsii.get(self, "description")

    @description.setter # type: ignore
    def description(self, value: builtins.str) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="executionRole")
    def execution_role(self) -> builtins.str:
        """``AWS::ServiceCatalog::StackSetConstraint.ExecutionRole``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-executionrole
        """
        return jsii.get(self, "executionRole")

    @execution_role.setter # type: ignore
    def execution_role(self, value: builtins.str) -> None:
        jsii.set(self, "executionRole", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="portfolioId")
    def portfolio_id(self) -> builtins.str:
        """``AWS::ServiceCatalog::StackSetConstraint.PortfolioId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-portfolioid
        """
        return jsii.get(self, "portfolioId")

    @portfolio_id.setter # type: ignore
    def portfolio_id(self, value: builtins.str) -> None:
        jsii.set(self, "portfolioId", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="productId")
    def product_id(self) -> builtins.str:
        """``AWS::ServiceCatalog::StackSetConstraint.ProductId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-productid
        """
        return jsii.get(self, "productId")

    @product_id.setter # type: ignore
    def product_id(self, value: builtins.str) -> None:
        jsii.set(self, "productId", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="regionList")
    def region_list(self) -> typing.List[builtins.str]:
        """``AWS::ServiceCatalog::StackSetConstraint.RegionList``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-regionlist
        """
        return jsii.get(self, "regionList")

    @region_list.setter # type: ignore
    def region_list(self, value: typing.List[builtins.str]) -> None:
        jsii.set(self, "regionList", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="stackInstanceControl")
    def stack_instance_control(self) -> builtins.str:
        """``AWS::ServiceCatalog::StackSetConstraint.StackInstanceControl``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-stackinstancecontrol
        """
        return jsii.get(self, "stackInstanceControl")

    @stack_instance_control.setter # type: ignore
    def stack_instance_control(self, value: builtins.str) -> None:
        jsii.set(self, "stackInstanceControl", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="acceptLanguage")
    def accept_language(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::StackSetConstraint.AcceptLanguage``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-acceptlanguage
        """
        return jsii.get(self, "acceptLanguage")

    @accept_language.setter # type: ignore
    def accept_language(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "acceptLanguage", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-servicecatalog.CfnStackSetConstraintProps",
    jsii_struct_bases=[],
    name_mapping={
        "account_list": "accountList",
        "admin_role": "adminRole",
        "description": "description",
        "execution_role": "executionRole",
        "portfolio_id": "portfolioId",
        "product_id": "productId",
        "region_list": "regionList",
        "stack_instance_control": "stackInstanceControl",
        "accept_language": "acceptLanguage",
    },
)
class CfnStackSetConstraintProps:
    def __init__(
        self,
        *,
        account_list: typing.List[builtins.str],
        admin_role: builtins.str,
        description: builtins.str,
        execution_role: builtins.str,
        portfolio_id: builtins.str,
        product_id: builtins.str,
        region_list: typing.List[builtins.str],
        stack_instance_control: builtins.str,
        accept_language: typing.Optional[builtins.str] = None,
    ) -> None:
        """Properties for defining a ``AWS::ServiceCatalog::StackSetConstraint``.

        :param account_list: ``AWS::ServiceCatalog::StackSetConstraint.AccountList``.
        :param admin_role: ``AWS::ServiceCatalog::StackSetConstraint.AdminRole``.
        :param description: ``AWS::ServiceCatalog::StackSetConstraint.Description``.
        :param execution_role: ``AWS::ServiceCatalog::StackSetConstraint.ExecutionRole``.
        :param portfolio_id: ``AWS::ServiceCatalog::StackSetConstraint.PortfolioId``.
        :param product_id: ``AWS::ServiceCatalog::StackSetConstraint.ProductId``.
        :param region_list: ``AWS::ServiceCatalog::StackSetConstraint.RegionList``.
        :param stack_instance_control: ``AWS::ServiceCatalog::StackSetConstraint.StackInstanceControl``.
        :param accept_language: ``AWS::ServiceCatalog::StackSetConstraint.AcceptLanguage``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "account_list": account_list,
            "admin_role": admin_role,
            "description": description,
            "execution_role": execution_role,
            "portfolio_id": portfolio_id,
            "product_id": product_id,
            "region_list": region_list,
            "stack_instance_control": stack_instance_control,
        }
        if accept_language is not None:
            self._values["accept_language"] = accept_language

    @builtins.property
    def account_list(self) -> typing.List[builtins.str]:
        """``AWS::ServiceCatalog::StackSetConstraint.AccountList``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-accountlist
        """
        result = self._values.get("account_list")
        assert result is not None, "Required property 'account_list' is missing"
        return result

    @builtins.property
    def admin_role(self) -> builtins.str:
        """``AWS::ServiceCatalog::StackSetConstraint.AdminRole``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-adminrole
        """
        result = self._values.get("admin_role")
        assert result is not None, "Required property 'admin_role' is missing"
        return result

    @builtins.property
    def description(self) -> builtins.str:
        """``AWS::ServiceCatalog::StackSetConstraint.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-description
        """
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return result

    @builtins.property
    def execution_role(self) -> builtins.str:
        """``AWS::ServiceCatalog::StackSetConstraint.ExecutionRole``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-executionrole
        """
        result = self._values.get("execution_role")
        assert result is not None, "Required property 'execution_role' is missing"
        return result

    @builtins.property
    def portfolio_id(self) -> builtins.str:
        """``AWS::ServiceCatalog::StackSetConstraint.PortfolioId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-portfolioid
        """
        result = self._values.get("portfolio_id")
        assert result is not None, "Required property 'portfolio_id' is missing"
        return result

    @builtins.property
    def product_id(self) -> builtins.str:
        """``AWS::ServiceCatalog::StackSetConstraint.ProductId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-productid
        """
        result = self._values.get("product_id")
        assert result is not None, "Required property 'product_id' is missing"
        return result

    @builtins.property
    def region_list(self) -> typing.List[builtins.str]:
        """``AWS::ServiceCatalog::StackSetConstraint.RegionList``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-regionlist
        """
        result = self._values.get("region_list")
        assert result is not None, "Required property 'region_list' is missing"
        return result

    @builtins.property
    def stack_instance_control(self) -> builtins.str:
        """``AWS::ServiceCatalog::StackSetConstraint.StackInstanceControl``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-stackinstancecontrol
        """
        result = self._values.get("stack_instance_control")
        assert result is not None, "Required property 'stack_instance_control' is missing"
        return result

    @builtins.property
    def accept_language(self) -> typing.Optional[builtins.str]:
        """``AWS::ServiceCatalog::StackSetConstraint.AcceptLanguage``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-acceptlanguage
        """
        result = self._values.get("accept_language")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnStackSetConstraintProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnTagOption(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-servicecatalog.CfnTagOption",
):
    """A CloudFormation ``AWS::ServiceCatalog::TagOption``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-tagoption.html
    :cloudformationResource: AWS::ServiceCatalog::TagOption
    """

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        key: builtins.str,
        value: builtins.str,
        active: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
    ) -> None:
        """Create a new ``AWS::ServiceCatalog::TagOption``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param key: ``AWS::ServiceCatalog::TagOption.Key``.
        :param value: ``AWS::ServiceCatalog::TagOption.Value``.
        :param active: ``AWS::ServiceCatalog::TagOption.Active``.
        """
        props = CfnTagOptionProps(key=key, value=value, active=active)

        jsii.create(CfnTagOption, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        """(experimental) Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.

        :stability: experimental
        """
        return jsii.invoke(self, "inspect", [inspector])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        """``AWS::ServiceCatalog::TagOption.Key``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-tagoption.html#cfn-servicecatalog-tagoption-key
        """
        return jsii.get(self, "key")

    @key.setter # type: ignore
    def key(self, value: builtins.str) -> None:
        jsii.set(self, "key", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        """``AWS::ServiceCatalog::TagOption.Value``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-tagoption.html#cfn-servicecatalog-tagoption-value
        """
        return jsii.get(self, "value")

    @value.setter # type: ignore
    def value(self, value: builtins.str) -> None:
        jsii.set(self, "value", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="active")
    def active(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        """``AWS::ServiceCatalog::TagOption.Active``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-tagoption.html#cfn-servicecatalog-tagoption-active
        """
        return jsii.get(self, "active")

    @active.setter # type: ignore
    def active(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "active", value)


@jsii.implements(aws_cdk.core.IInspectable)
class CfnTagOptionAssociation(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-servicecatalog.CfnTagOptionAssociation",
):
    """A CloudFormation ``AWS::ServiceCatalog::TagOptionAssociation``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-tagoptionassociation.html
    :cloudformationResource: AWS::ServiceCatalog::TagOptionAssociation
    """

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        resource_id: builtins.str,
        tag_option_id: builtins.str,
    ) -> None:
        """Create a new ``AWS::ServiceCatalog::TagOptionAssociation``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param resource_id: ``AWS::ServiceCatalog::TagOptionAssociation.ResourceId``.
        :param tag_option_id: ``AWS::ServiceCatalog::TagOptionAssociation.TagOptionId``.
        """
        props = CfnTagOptionAssociationProps(
            resource_id=resource_id, tag_option_id=tag_option_id
        )

        jsii.create(CfnTagOptionAssociation, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        """(experimental) Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.

        :stability: experimental
        """
        return jsii.invoke(self, "inspect", [inspector])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="resourceId")
    def resource_id(self) -> builtins.str:
        """``AWS::ServiceCatalog::TagOptionAssociation.ResourceId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-tagoptionassociation.html#cfn-servicecatalog-tagoptionassociation-resourceid
        """
        return jsii.get(self, "resourceId")

    @resource_id.setter # type: ignore
    def resource_id(self, value: builtins.str) -> None:
        jsii.set(self, "resourceId", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="tagOptionId")
    def tag_option_id(self) -> builtins.str:
        """``AWS::ServiceCatalog::TagOptionAssociation.TagOptionId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-tagoptionassociation.html#cfn-servicecatalog-tagoptionassociation-tagoptionid
        """
        return jsii.get(self, "tagOptionId")

    @tag_option_id.setter # type: ignore
    def tag_option_id(self, value: builtins.str) -> None:
        jsii.set(self, "tagOptionId", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-servicecatalog.CfnTagOptionAssociationProps",
    jsii_struct_bases=[],
    name_mapping={"resource_id": "resourceId", "tag_option_id": "tagOptionId"},
)
class CfnTagOptionAssociationProps:
    def __init__(
        self,
        *,
        resource_id: builtins.str,
        tag_option_id: builtins.str,
    ) -> None:
        """Properties for defining a ``AWS::ServiceCatalog::TagOptionAssociation``.

        :param resource_id: ``AWS::ServiceCatalog::TagOptionAssociation.ResourceId``.
        :param tag_option_id: ``AWS::ServiceCatalog::TagOptionAssociation.TagOptionId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-tagoptionassociation.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "resource_id": resource_id,
            "tag_option_id": tag_option_id,
        }

    @builtins.property
    def resource_id(self) -> builtins.str:
        """``AWS::ServiceCatalog::TagOptionAssociation.ResourceId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-tagoptionassociation.html#cfn-servicecatalog-tagoptionassociation-resourceid
        """
        result = self._values.get("resource_id")
        assert result is not None, "Required property 'resource_id' is missing"
        return result

    @builtins.property
    def tag_option_id(self) -> builtins.str:
        """``AWS::ServiceCatalog::TagOptionAssociation.TagOptionId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-tagoptionassociation.html#cfn-servicecatalog-tagoptionassociation-tagoptionid
        """
        result = self._values.get("tag_option_id")
        assert result is not None, "Required property 'tag_option_id' is missing"
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTagOptionAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-servicecatalog.CfnTagOptionProps",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value", "active": "active"},
)
class CfnTagOptionProps:
    def __init__(
        self,
        *,
        key: builtins.str,
        value: builtins.str,
        active: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
    ) -> None:
        """Properties for defining a ``AWS::ServiceCatalog::TagOption``.

        :param key: ``AWS::ServiceCatalog::TagOption.Key``.
        :param value: ``AWS::ServiceCatalog::TagOption.Value``.
        :param active: ``AWS::ServiceCatalog::TagOption.Active``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-tagoption.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "value": value,
        }
        if active is not None:
            self._values["active"] = active

    @builtins.property
    def key(self) -> builtins.str:
        """``AWS::ServiceCatalog::TagOption.Key``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-tagoption.html#cfn-servicecatalog-tagoption-key
        """
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return result

    @builtins.property
    def value(self) -> builtins.str:
        """``AWS::ServiceCatalog::TagOption.Value``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-tagoption.html#cfn-servicecatalog-tagoption-value
        """
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return result

    @builtins.property
    def active(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        """``AWS::ServiceCatalog::TagOption.Active``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-tagoption.html#cfn-servicecatalog-tagoption-active
        """
        result = self._values.get("active")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTagOptionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAcceptedPortfolioShare",
    "CfnAcceptedPortfolioShareProps",
    "CfnCloudFormationProduct",
    "CfnCloudFormationProductProps",
    "CfnCloudFormationProvisionedProduct",
    "CfnCloudFormationProvisionedProductProps",
    "CfnLaunchNotificationConstraint",
    "CfnLaunchNotificationConstraintProps",
    "CfnLaunchRoleConstraint",
    "CfnLaunchRoleConstraintProps",
    "CfnLaunchTemplateConstraint",
    "CfnLaunchTemplateConstraintProps",
    "CfnPortfolio",
    "CfnPortfolioPrincipalAssociation",
    "CfnPortfolioPrincipalAssociationProps",
    "CfnPortfolioProductAssociation",
    "CfnPortfolioProductAssociationProps",
    "CfnPortfolioProps",
    "CfnPortfolioShare",
    "CfnPortfolioShareProps",
    "CfnResourceUpdateConstraint",
    "CfnResourceUpdateConstraintProps",
    "CfnStackSetConstraint",
    "CfnStackSetConstraintProps",
    "CfnTagOption",
    "CfnTagOptionAssociation",
    "CfnTagOptionAssociationProps",
    "CfnTagOptionProps",
]

publication.publish()
