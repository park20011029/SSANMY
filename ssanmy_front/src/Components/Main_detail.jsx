import React from "react";
import "../styleCss/Main.css";

function Main_detail() {
    return (
        <div className="main">
            <div className="p_categori_word">인기 카테고리</div>
            <div className="p_categori">
                <div className="categori_box">
                    <div className="categori_circle"></div>
                    <div className="categori_name">카테고리</div>
                </div>
                <div className="categori_box">
                    <div className="categori_circle"></div>
                    <div className="categori_name">카테고리</div>
                </div>
                <div className="categori_box">
                    <div className="categori_circle"></div>
                    <div className="categori_name">카테고리</div>
                </div>
                <div className="categori_box">
                    <div className="categori_circle"></div>
                    <div className="categori_name">카테고리</div>
                </div>
                <div className="categori_box">
                    <div className="categori_circle"></div>
                    <div className="categori_name">카테고리</div>
                </div>
            </div>
            <div className="ex_mods">
                <div className="ex_mod_box"></div>
                <div className="ex_mod_box"></div>
                <div className="ex_mod_box"></div>
                <div className="ex_mod_box"></div>
                <div className="ex_mod_box"></div>
                {/*{% if mods_list %}*/}
                {/*<ul>*/}
                    {/*{% for mod in mods_list %}*/}
                    {/*<li><a href="/ssanmy/{{ mod.id }}/">{{mod.post_title}}</a></li>*/}
                    {/*{% endfor %}*/}
                {/*</ul>*/}
                {/*{% else %}*/}
                {/*{% endif %}*/}
            </div>
        </div>

    )
}

export default Main_detail;