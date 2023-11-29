<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <xsl:template match="/">
        <html>
            <body>
                <h1 class="text-center">Organization Information Preview</h1>
                <table>
                    <xsl:for-each select="data">
                    <tr>
                        <th class="colwidth">Organization Name</th>
                        <td class="colwidth"><xsl:value-of select="orgName"/></td>
                    </tr>
                    <tr>
                        <th class="colwidth">Organization Email</th>
                        <td class="colwidth"><xsl:value-of select="orgEmail"/></td>
                    </tr>
                    <tr>
                        <th class="colwidth">Organization Contact Number</th>
                        <td class="colwidth"><xsl:value-of select="orgContact"/></td>
                    </tr>
                    <tr>
                        <th class="colwidth">Organization Address</th>
                        <td class="colwidth"><xsl:value-of select="orgAddress"/></td>
                    </tr>
                    <tr>
                        <th class="colwidth">Authorized Person Name</th>
                        <td class="colwidth"><xsl:value-of select="adminName"/></td>
                    </tr>
                    <tr>
                        <th class="colwidth">Designation</th>
                        <td class="colwidth"><xsl:value-of select="adminDesig"/></td>
                    </tr>
                    <tr>
                        <th class="colwidth">Official Email</th>
                        <td class="colwidth"><xsl:value-of select="adminEmail"/></td>
                    </tr>
                    <tr>
                        <th class="colwidth">Contact Number</th>
                        <td class="colwidth"><xsl:value-of select="adminContact"/></td>
                    </tr>
                    <tr>
                        <td></td>
                    </tr>
                    <tr>
                        <td colspan="2" class="colwidth text-center">
                            <button class="proceedBtn">Proceed with e-Sign</button>
                            <button class="proceedBtn">Proceed without e-Sign</button>
                        </td>
                    </tr>
                    </xsl:for-each>
                </table>            
            </body>
        </html>
    </xsl:template>

</xsl:stylesheet>
