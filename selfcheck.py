# -*- coding: utf-8 -*-
"""无头自检（不开窗口）：验证码生成 + 正确/错误判定 + 滑块数据生成。

用法：python selfcheck.py    （退出 0 = 通过）
GUI 入口仍是 `python main.py`。
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from model.captcha_model import CaptchaConfig  # noqa: E402
from viewmodel.captcha_viewmodel import SliderCaptchaViewModel, TextCaptchaViewModel  # noqa: E402


def main() -> int:
    config = CaptchaConfig()
    config.load(str(ROOT / "config" / "captcha_config.json"))

    # 1) 文字验证码：生成 → 正确码通过 → 错误码不通过
    text_vm = TextCaptchaViewModel(config)
    text_vm.create()
    data = text_vm.model.text_data
    if data is None or not data.code:
        print("FAIL text captcha not generated")
        return 1
    if text_vm.model.verify(data.code).success is not True:
        print("FAIL correct answer rejected")
        return 1
    wrong = "0000" if data.code != "0000" else "1111"
    if text_vm.model.verify(wrong).success:
        print("FAIL wrong answer accepted")
        return 1

    # 2) 滑块验证码：生成缺口与滑块数据
    slider_vm = SliderCaptchaViewModel(config)
    slider_vm.create()
    slider = slider_vm.model.slider_data
    if slider is None:
        print("FAIL slider captcha not generated")
        return 1

    print(f"captcha selfcheck ok: text[{len(data.code)}] + slider + verdicts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
