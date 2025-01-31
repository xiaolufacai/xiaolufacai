(function () {
    var minIntervalTime = 100;  // 最小点击间隔（毫秒）
    var maxIntervalTime = 500;  // 最大点击间隔（毫秒）
    var positionJitter = 5;     // 点击位置的随机抖动范围（像素）
    var currentX = 0;           // 鼠标的 X 坐标
    var currentY = 0;           // 鼠标的 Y 坐标

    // 配置项（可以动态调整）
    var config = {
        minIntervalTime: 100,  // 最小点击间隔
        maxIntervalTime: 500,  // 最大点击间隔
        positionJitter: 5,     // 点击位置的随机抖动范围（像素）
        pathJitter: 20,        // 鼠标路径的随机波动范围（像素）
        maxHoverDuration: 200 // 最大悬停时间（毫秒）
    };

    // 监听鼠标移动，实时更新坐标
    document.addEventListener("mousemove", function (event) {
        currentX = event.clientX;
        currentY = event.clientY;
    });

    // 生成随机偏移量（用于位置抖动）
    function getRandomOffset(maxOffset) {
        return Math.floor(Math.random() * (maxOffset * 2 + 1)) - maxOffset;
    }

    // 生成鼠标移动的路径（模拟不规则轨迹）
    function getRandomMousePath(x, y, jitter) {
        var path = [];
        var steps = Math.floor(Math.random() * 5) + 5; // 生成随机数量的路径点（5到10个）
        for (var i = 0; i < steps; i++) {
            var newX = x + getRandomOffset(jitter);
            var newY = y + getRandomOffset(jitter);
            path.push([newX, newY]);
        }
        return path;
    }

    // 鼠标移动模拟
    function moveMouseAlongPath(path, index = 0) {
        if (index >= path.length) return;

        var [newX, newY] = path[index];
        var mousemoveEvent = new MouseEvent("mousemove", {
            bubbles: true,
            cancelable: true,
            view: window,
            clientX: newX,
            clientY: newY,
        });

        document.dispatchEvent(mousemoveEvent);
        setTimeout(() => moveMouseAlongPath(path, index + 1), 20); // 每次移动稍微延迟，模拟鼠标移动的自然速度
    }

    // 创建并触发鼠标事件
    function triggerMouseEvent(targetElement, eventType, x, y) {
        try {
            var event = new MouseEvent(eventType, {
                bubbles: true,
                cancelable: true,
                view: window,
                clientX: x,
                clientY: y,
            });
            targetElement.dispatchEvent(event);
        } catch (error) {
            console.error(`触发 ${eventType} 事件失败：`, error);
        }
    }

    // 模拟点击
    function simulateClickAtPosition(x, y) {
        try {
            var targetElement = document.elementFromPoint(x, y); // 获取鼠标位置的目标元素
            if (targetElement) {
                triggerMouseEvent(targetElement, "mousedown", x, y);
                triggerMouseEvent(targetElement, "mouseup", x, y);
                triggerMouseEvent(targetElement, "click", x, y);

                console.log(`在 (${x}, ${y}) 对目标 ${targetElement.tagName} 触发了一次点击`);
            } else {
                console.warn(`在 (${x}, ${y}) 未找到目标，跳过点击`);
            }
        } catch (error) {
            console.error("点击失败：", error);
        }
    }

    // 模拟人类点击逻辑
    function humanLikeClick() {
        // 随机生成鼠标移动路径
        var mousePath = getRandomMousePath(currentX, currentY, config.pathJitter);
        moveMouseAlongPath(mousePath); // 模拟鼠标移动

        // 模拟点击前的短暂悬停（停留1-2秒）
        var hoverDuration = Math.floor(Math.random() * config.maxHoverDuration) + 500;
        setTimeout(() => {
            // 添加位置抖动
            var jitteredX = currentX + getRandomOffset(config.positionJitter);
            var jitteredY = currentY + getRandomOffset(config.positionJitter);

            // 模拟点击
            simulateClickAtPosition(jitteredX, jitteredY);

            // 随机生成下一个点击的间隔时间
            var nextIntervalTime = Math.floor(Math.random() * (config.maxIntervalTime - config.minIntervalTime + 1)) + config.minIntervalTime;

            // 设置下一个点击
            setTimeout(humanLikeClick, nextIntervalTime);

        }, hoverDuration); // 模拟点击前的悬停
    }

    // 启动点击
    humanLikeClick();
    console.log("模拟人类点击已启动！");
})();
