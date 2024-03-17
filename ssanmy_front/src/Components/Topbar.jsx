import React from "react";
import "../styleCss/Topbar.css"
function Topbar() {
    return (
        <div>
            <div class="topbar">
                    <div class="logo">
                        <img class="logoImg" src="https://projectmanager4.s3.ap-northeast-2.amazonaws.com/logo_fix.svg" alt="로고"/>
                    </div>
                    <div class="search_bar">
                        <div class="search_text">
                            <input type="text" placeholder="search"/>
                        </div>
                        <div class="search_btn">
                            <img src="https://projectmanager4.s3.ap-northeast-2.amazonaws.com/search_parkmin.svg" alt="로고"/>
                        </div>
                    </div>
                    <div class="search_btn">
                            <img src="https://projectmanager4.s3.ap-northeast-2.amazonaws.com/search_parkmin.svg" alt="로고"/>
                    </div>
                    <div class="profile_btn">
                            <img src="https://projectmanager4.s3.ap-northeast-2.amazonaws.com/user+1.svg" alt="로고"/>
                    </div>
            </div>
            <div class="notFix">
                <div><span>홈</span></div>
                <div><span>전자 제품</span></div>
                <div><span>전자 제품</span></div>
                <div><span>전자 제품</span></div>
                <div><span>전자 제품</span></div>
                <div><span>전자 제품</span></div>
                <div><span>전자 제품</span></div>
            </div>
        </div>
    )
}

export default Topbar;