<div style="margin:0px;padding: 0px;">
    <p style="padding:0px;font-size: 13px;">

        Estimado/a ${object.partner_id.name}
        % if object.partner_id.parent_id:
            (${object.partner_id.parent_id.name})
        % endif

        <br>
        <br>
        
        % if object.invoice_payment_state == 'cancel' or object.l10n_mx_edi_pac_status == 'cancelled' or object.l10n_mx_edi_sat_status == 'cancelled':
            Su factura ha sido cancelada
        
        % else:
            Se 
            % if object.number:
                adjunta su factura <strong>${object.number}</strong>
            % else:
                adjunta su factura
            %endif

            % if object.origin:
                (con referencia: ${object.origin})
            % endif
            
            por un importe de  <strong>${format_amount(object.amount_total, object.currency_id)}</strong>
            de ${object.company_id.name}
            
            % if object.invoice_payment_state == 'paid':
                Esta factura ya se encuentra pagada. Gracias por realizar el pago correspondiente.
            % else:
                Por favor, remita su pago tan pronto como le sea posible.
            <br>
                <br></p><p style="padding:0px;font-size: 13px;">Los datos bancarios para realizar pago son:

            % endif
        
        <br>
        <br>

            % if object.invoice_payment_state == 'not_paid':
                % if object.company_id.currency_id == 'MXN':
                    ${object.company_id.x_pesos_account} 
                    
                % else:
                    </p><p><b><span class="o_field_char o_field_widget o_required_modifier" name="name" style="margin:0 0 0px 0;text-align:left;">BBVA BANCOMER</span></b></p><p><b>${object.company_id.name}
                    </b></p><p>CUENTA: ${object.company_id.x_dollars_account[18:28]}
                    </p><p>CLABE INT. ${object.company_id.x_dollars_account[35:]}
                    </p><p>CLABE SUC.0018
                        
                % endif
</p><p><br></p><p>                Favor de enviar el comprobante de pago al correo: facturacion@ambit.com.mx &nbsp;como referencia colocar: <b>${object.name}</b>
            % endif 
        % endif
  
        </p><br>
        
        
        En caso de requerir cualquier aclaración, por
        favor no dude en contactarnos.
        <br><br><p><a name="_MailAutoSig"><b><span style="color:gray">ALEJANDRA DURAN<br></span></b></a></p><p>

</p><p><b>&nbsp;</b></p><p>

</p><p><span style="color:gray">AMBIT
TECHNOLOGY</span></p><p>

</p><p><span style="color:gray">LAGO
ESTEFANÍA 31, 4to. PISO
COL. GRANADA, CP. 11520, CIUDAD DE MÉXICO</span><span style="color:#7F7F7F" lang="ES">.</span><span style="color:gray"></span></p><p>

</p><p><span style="color:#7F7F7F" lang="ES">
</span><span style="color:red" lang="ES">T.</span><span style="color:#7F7F7F" lang="ES">&nbsp;(55) 1054.1023/&nbsp;</span><span style="color:red" lang="ES">C. </span><span style="color:#7F7F7F" lang="ES">&nbsp;(044) 55 7665.4211 /&nbsp;</span><span style="color:red" lang="ES">F.</span><span style="color:#7F7F7F" lang="ES">&nbsp;(55) 1054.1024</span></p><p>

</p><p><span style="color:red" lang="ES">M.</span><span style="color:gray"> recepcion</span><a href="mailto:gpareja@ambit.com.mx"><span style="color:gray" lang="ES">@ambit.com.mx</span></a><span style="color:#7F7F7F" lang="ES"> / </span><span style="color:red" lang="ES">W. </span><a href="http://www.ambit.com.mx/"><span style="color:gray" lang="ES">www.ambit.com.mx</span></a><br><img style="vertical-align: middle; width: 118px; height: auto;" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHYAAAA7CAMAAACZv46RAAAAaVBMVEXjIhnlMCfnPjboTETqWVPsZ2HudXDvg36amp2goKOnp6mtra+zs7a6urzxkIzznpr0rKj2urfAwMLGxsjMzM7T09TZ2drf3+D4yMX61dTm5ubs7O374+Ly8vP98fH+/v78A/sAAAD////0CvYiAAAAIXRSTlP//////////////////////////////////////////wCfwdAhAAADyElEQVR4nO2Z25qjIAyAW3u0hI5VYBRq4f2fckFAQO1WbXdudnLRjwDNLwGCxI2aFE4ryM9Wcigpn+62WjbjKsnweSQ5ZvJfYnk1ZjopPzfmAZaDsY8wYTwwOKcEI9MAnwIn2Ba0M5/OI6d6uqH9OJagSrzoLipEP4wVr5hW+Lxus7GrREAnU00t78SrVpOfwXK7yKeaSNpkNf6L/cWuxrJ0kf8UdiD/O/a093L6uvtu99qIUW+m/XRz9Z12LB5DbEsxACYhdIYo1ZVsR2qKwmL3m0j2tf3XtdOuqs5cQ9YYqNe2twQrS38qX3w4DCuZnFOBCexmU8TYItRvG3WKut0irESRVbYOaw1a7C6uz4pY2z4CFiVm2TpsFrB/kyJgU8nbWVgvj9suDLfHHuu6yHrW/lYXrtchwWLGGbhymWI50eJaTJGNNpC1eI2wX92y3vpn6B4v653SY+1Lh3/nlGpZcLzZIQXsztYfnfvtvnErK8IS9/9LmN1FMXmILWy1005Wq4fY3P+dWb2ajbXhwRrcBtA9wdZPsJW3Iv2imYNtTslG6Qxe+1KEfTzBsv7p7VZCM7D34QaKsFmKVU+wISTCcNs8wzbbETVg9/OwPXU29uGp2f5wvV7XYZeP1hk8NK5iFTZcYObOrd36R9f4WIgV6bb1K/k11lrwx+xtIVYFTCd07r5N7PlTYT4Wp15GYUNNYunkaL+WrmQflnK7qBwqj8opFjzWLuSdiT93F3mXYN1knnPWKuFPAjKBdX4gUvFSYz0q20eRaj7Wz2YicgIbJyc09p5Ei+1hKVaVQ2jqcI9tU6wqYmxh7TcLsCOuix0DrF8FHqua3ru7xtmvl2AVu0RQ7BNJQ6xieYLVZo564+yO5l2muRq5+4PQxS5/LDrtkWjGYpc9ywGzkFIZ3OZNDUW6F0Lk7VvBSvnF/mLnyjhXJqfShZ/GjhNjnEx0exsrWKL+EFYgBOobgJiksP5FFegjviKAhZIE4NtgBQbc6iswYCqw/lP1/mi11RZJhTnTllulz/uSKs3noEqiZN7qDkgoflElUyLn5bcSyY1vXYZVW6VACBCbaYauBrrSRf8ywgk3F0DMzYsPcPM46Y1vRj6Zj/LJGkKIDr0tyCEWeax5s6ocVg8dLcye4/yMh9uBd/40dskQqxkScU7aXGr3KhDGyfq4onO/FbDn3wraHLSbAAkJSK+mGCt0NTUqy3V7t7DMPV8/xMSXkdHLQi8vp+C1aP9S45URVj//k+9A736coCUBpihqp7FGOC0//9VLcE20lv4A74GG1OOUraoAAAAASUVORK5CYII=" data-filename="image.png"><br></p><p>

</p><p>

</p><p><span style="color:#7F7F7F" lang="ES">
</span><span style="color:#002060" lang="ES">"EXCELENTE&nbsp;<b>ACTITUD</b>, EXCELENTE&nbsp;<b>SERVICIO</b>"</span></p><p>

</p><p><span style="color:#A6A6A6" lang="ES">_________________________________________________________________________________________________</span></p><p>

</p><p><span style="color:gray" lang="ES">Este mensaje (y cualquier
archivo adjunto) puede contener información privilegiada/confidencial. Si usted
no es el destinatario indicado en este mensaje no está autorizado a copiar o
entregar este mensaje a nadie mas. En tal caso, debe destruir éste mensaje y
notificar al remitente vía correo electrónico, a la dirección indicada.</span></p><p>

</p><p><span style="color:gray" lang="EN-US">This message (and it´s
attachments) may have privileged/confidential information. If this message was
not intended for you, then you are not authorized to copy or forward this
message to anyone else. In such case, you should delete this message and notify
the sender by e-mail.</span></p><br>
</div>