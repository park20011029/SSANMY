import React from "react";
import "../styleCss/Model_detail.css";

function Model_detail () {
    return (
        <div className="model_main">
            <div className="model_name">
                대충 상품명
            </div>
            <div className="model_explain">
                <img className="model_img" src="//thumbnail10.coupangcdn.com/thumbnails/remote/230x230ex/image/retail/images/1742738348078382-1202e905-701f-4e63-b94c-897babcc7464.jpg"></img>
                <div className="model_info">
                    <div className="model_info_box">
                        대충 설명
                    </div>
                </div>
            </div>

            <div className="model_drive">
                <div className="model_drive_box">
                    대충 배송비
                </div>
            </div>
            <div className="comment_word">
                COMMENT
            </div>
            <hr/>

            <div className="">
                
            </div>

        </div>
    )
}

export default Model_detail;