<%@ Page language="C#"   Inherits="Microsoft.SharePoint.Publishing.PublishingLayoutPage,Microsoft.SharePoint.Publishing,Version=14.0.0.0,Culture=neutral,PublicKeyToken=71e9bce111e9429c" meta:progid="SharePoint.WebPartPage.Document"  %>
<%@ Register Tagprefix="SharePointWebControls" Namespace="Microsoft.SharePoint.WebControls" Assembly="Microsoft.SharePoint, Version=14.0.0.0, Culture=neutral, PublicKeyToken=71e9bce111e9429c" %> <%@ Register Tagprefix="WebPartPages" Namespace="Microsoft.SharePoint.WebPartPages" Assembly="Microsoft.SharePoint, Version=14.0.0.0, Culture=neutral, PublicKeyToken=71e9bce111e9429c" %> <%@ Register Tagprefix="PublishingWebControls" Namespace="Microsoft.SharePoint.Publishing.WebControls" Assembly="Microsoft.SharePoint.Publishing, Version=14.0.0.0, Culture=neutral, PublicKeyToken=71e9bce111e9429c" %> <%@ Register Tagprefix="PublishingNavigation" Namespace="Microsoft.SharePoint.Publishing.Navigation" Assembly="Microsoft.SharePoint.Publishing, Version=14.0.0.0, Culture=neutral, PublicKeyToken=71e9bce111e9429c" %>
<%@ Register TagPrefix="WpNs0" Namespace="Microsoft.SharePoint.Portal.WebControls" Assembly="Microsoft.Office.Server.Search, Version=14.0.0.0, Culture=neutral, PublicKeyToken=71e9bce111e9429c"%>
<%@ Register Tagprefix="SharePoint" Namespace="Microsoft.SharePoint.WebControls" Assembly="Microsoft.SharePoint, Version=14.0.0.0, Culture=neutral, PublicKeyToken=71e9bce111e9429c" %> <%@ Register Tagprefix="Utilities" Namespace="Microsoft.SharePoint.Utilities" Assembly="Microsoft.SharePoint, Version=14.0.0.0, Culture=neutral, PublicKeyToken=71e9bce111e9429c" %> <%@ Register Tagprefix="WebPartPages" Namespace="Microsoft.SharePoint.WebPartPages" Assembly="Microsoft.SharePoint, Version=14.0.0.0, Culture=neutral, PublicKeyToken=71e9bce111e9429c" %> <%@ Register Tagprefix="OSRVWC" Namespace="Microsoft.Office.Server.WebControls" Assembly="Microsoft.Office.Server, Version=14.0.0.0, Culture=neutral, PublicKeyToken=71e9bce111e9429c" %> <%@ Register Tagprefix="OSRVUPWC" Namespace="Microsoft.Office.Server.WebControls" Assembly="Microsoft.Office.Server.UserProfiles, Version=14.0.0.0, Culture=neutral, PublicKeyToken=71e9bce111e9429c" %> <%@ Register Tagprefix="SPSWC" Namespace="Microsoft.SharePoint.Portal.WebControls" Assembly="Microsoft.SharePoint.Portal, Version=14.0.0.0, Culture=neutral, PublicKeyToken=71e9bce111e9429c" %> <%@ Register Tagprefix="SEARCHWC" Namespace="Microsoft.Office.Server.Search.WebControls" Assembly="Microsoft.Office.Server.Search, Version=14.0.0.0, Culture=neutral, PublicKeyToken=71e9bce111e9429c" %> <%@ Register Tagprefix="PublishingWebControls" Namespace="Microsoft.SharePoint.Publishing.WebControls" Assembly="Microsoft.SharePoint.Publishing, Version=14.0.0.0, Culture=neutral, PublicKeyToken=71e9bce111e9429c" %>

<asp:Content ContentPlaceholderID="PlaceHolderPageTitle" runat="server">


<SharePointWebControls:FieldValue id="PageTitle" FieldName="Title" runat="server"/>
</asp:Content>
<asp:Content ContentPlaceholderID="PlaceHolderMain" runat="server">
<style type="text/css">
	.s4-ca 
	{
	  margin-left:0px!important;
	}


	#s4-leftpanel 
	{
	  display:none;
	}

    .s4-titletext H2
    {
	  display:none;
    }

    .ms-ptabarea
    {
        padding-bottom: 15px;
    }
   


</style>
<WebPartPages:spproxywebpartmanager runat="server" id="spproxywebpartmanager"></WebPartPages:SPProxyWebPartManager>
  <table cellpadding="4" cellspacing="0" border="0" width="100%" height="100%">
    <tr>
      <td class="esw-layoutA-leftzone" valign="top" rowspan="2" >
        <div class="esw-layoutA-leftzonecontent">
          <WebPartPages:webpartzone id="Zone1" runat="server" title="Zone 1"><ZoneTemplate></ZoneTemplate></WebPartPages:webpartzone>
        </div>

      </td>
      <td class="esw-layoutA-centerzone" valign="top" colspan="2">
        <div class="esw-searchcontrols">
                  <SharePoint:UIVersionedContent UIVersion="3" runat="server">
          <ContentTemplate>
          <SPSWC:ListBoundTabStrip ID="Tab" runat="server" PersistQueryString="true" CSSClassNamePrefix="ms-sctab" ListName="<%$Resources:Microsoft.Office.Server.Search,SearchCenterOnet_SearchCenterListName%>" ResourceIdforListName="$Resources:Microsoft.Office.Server.Search,SearchCenterOnet_SearchCenterListName" UnselectedTabTrimLength="-1"></SPSWC:ListBoundTabStrip>
            </ContentTemplate>
          </SharePoint:UIVersionedContent>
          <SharePoint:UIVersionedContent UIVersion="4" runat="server">
          <ContentTemplate>
        
          <SPSWC:ListBoundTabStrip ID="Tab1" runat="server" CSSFileName="Themable/search.css" PersistQueryString="true" CSSClassNamePrefix="ms-sctab" ListName="<%$Resources:Microsoft.Office.Server.Search,SearchCenterOnet_SearchCenterListName%>" ResourceIdforListName="$Resources:Microsoft.Office.Server.Search,SearchCenterOnet_SearchCenterListName" UnselectedTabTrimLength="-1"></SPSWC:ListBoundTabStrip>
          
            </ContentTemplate>
          </SharePoint:UIVersionedContent>
          
          <WebPartPages:WebPartZone id="ZoneSearch" runat="server" title="Zone Search"><ZoneTemplate></ZoneTemplate></WebPartPages:WebPartZone>

          
          
        </div>
      </td>
      <td class="esw-layoutA-rightzone" valign="top">
        
          <div align="center" class="esw-FEMASearchLogo">
                              <img src="_layouts/DHS.FEMA.SharePoint.ESWBranding/images/search.png" alt="SearchLogo" width="150px" />
                  </div>
                  
        

      </td>
    </tr>
    <tr>
      <td class="esw-layoutASub-leftzone" valign="top" >
        <div class="esw-layoutA-leftzonecontent">
          <WebPartPages:webpartzone id="g_35EDBFD57CC9443F9FBCC2A4BE251925" runat="server" title="Zone 1"><ZoneTemplate></ZoneTemplate></WebPartPages:webpartzone>
        </div>

      </td>
      <td class="esw-layoutASub-centerzone" valign="top" >
        <div class="esw-layoutA-centerzonecontent">
        <WebPartPages:webpartzone id="g_B206CFC79A814E1C9C55DA920F149B89" runat="server" title="Zone 2"><ZoneTemplate></ZoneTemplate></WebPartPages:webpartzone>
        
        </div>

      </td>
      <td class="esw-layoutASub-rightzone" valign="top">
        <div class="esw-layoutA-rightzonecontent">
    
          <WebPartPages:webpartzone id="g_A5E2B6AC8D5B4FBFA8F0E5562002C8F2" runat="server" title="Zone 3"><ZoneTemplate></ZoneTemplate></WebPartPages:webpartzone>
          
        </div>

      </td>
    </tr>

  </table>
</asp:Content>

