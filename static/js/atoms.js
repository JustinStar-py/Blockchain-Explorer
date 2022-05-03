if (screen.width > 600){ 
   document.addEventListener("DOMContentLoaded", function() {
    particleground(document.getElementById("particles"), {
        dotColor: "#EFEFEF",
        lineColor: "#fff"
    });
    var t = document.getElementById("intro");
    t.style.marginTop = -t.offsetHeight / 2 + "px"
   }, !1),
   function(Y, O) {
    "use strict";
    var M = "particleground",
        S = Y.jQuery;

    function n(s, o) {
        var r, n, i, a, h, p, l = !!O.createElement("canvas").getContext,
            d = [],
            f = 0,
            c = 0,
            x = !navigator.userAgent.match(/(iPhone|iPod|iPad|Android|BlackBerry|BB10|mobi|tablet|opera mini|nexus 7)/i),
            u = !!Y.DeviceOrientationEvent,
            m = 0,
            y = 0,
            e = !1;

        function g() {
            r.width = s.offsetWidth, r.height = s.offsetHeight, n.fillStyle = o.dotColor, n.strokeStyle = o.lineColor, n.lineWidth = o.lineWidth
        }

        function w() {
            if (l) {
                i = Y.innerWidth, a = Y.innerHeight, n.clearRect(0, 0, r.width, r.height);
                for (var t = 0; t < d.length; t++) d[t].updatePosition();
                for (t = 0; t < d.length; t++) d[t].draw();
                e || requestAnimationFrame(w)
            }
        }

        function v() {
            switch (this.stackPos, this.active = !0, this.layer = Math.ceil(3 * Math.random()), this.parallaxOffsetX = 0, this.parallaxOffsetY = 0, this.position = {
                    x: Math.ceil(Math.random() * r.width),
                    y: Math.ceil(Math.random() * r.height)
                }, this.speed = {}, o.directionX) {
                case "left":
                    this.speed.x = +(-o.maxSpeedX + Math.random() * o.maxSpeedX - o.minSpeedX).toFixed(2);
                    break;
                case "right":
                    this.speed.x = +(Math.random() * o.maxSpeedX + o.minSpeedX).toFixed(2);
                    break;
                default:
                    this.speed.x = +(-o.maxSpeedX / 2 + Math.random() * o.maxSpeedX).toFixed(2), this.speed.x += 0 < this.speed.x ? o.minSpeedX : -o.minSpeedX
            }
            switch (o.directionY) {
                case "up":
                    this.speed.y = +(-o.maxSpeedY + Math.random() * o.maxSpeedY - o.minSpeedY).toFixed(2);
                    break;
                case "down":
                    this.speed.y = +(Math.random() * o.maxSpeedY + o.minSpeedY).toFixed(2);
                    break;
                default:
                    this.speed.y = +(-o.maxSpeedY / 2 + Math.random() * o.maxSpeedY).toFixed(2), this.speed.x += 0 < this.speed.y ? o.minSpeedY : -o.minSpeedY
            }
        }

        function X(t) {
            void 0 !== o[t] && o[t].call(s)
        }
        return o = function(t) {
                t = t || {};
                for (var e = 1; e < arguments.length; e++) {
                    var i = arguments[e];
                    if (i)
                        for (var a in i) i.hasOwnProperty(a) && ("object" == typeof i[a] ? deepExtend(t[a], i[a]) : t[a] = i[a])
                }
                return t
            }({}, Y[M].defaults, o), v.prototype.draw = function() {
                n.beginPath(), n.arc(this.position.x + this.parallaxOffsetX, this.position.y + this.parallaxOffsetY, o.particleRadius / 2, 0, 2 * Math.PI, !0), n.closePath(), n.fill(), n.beginPath();
                for (var t = d.length - 1; t > this.stackPos; t--) {
                    var e = d[t],
                        i = this.position.x - e.position.x,
                        a = this.position.y - e.position.y;
                    Math.sqrt(i * i + a * a).toFixed(2) < o.proximity && (n.moveTo(this.position.x + this.parallaxOffsetX, this.position.y + this.parallaxOffsetY), o.curvedLines ? n.quadraticCurveTo(Math.max(e.position.x, e.position.x), Math.min(e.position.y, e.position.y), e.position.x + e.parallaxOffsetX, e.position.y + e.parallaxOffsetY) : n.lineTo(e.position.x + e.parallaxOffsetX, e.position.y + e.parallaxOffsetY))
                }
                n.stroke(), n.closePath()
            }, v.prototype.updatePosition = function() {
                o.parallax && (p = u && !x ? (h = (m - -30) * (+i / 60) + 0, (y - -30) * (+a / 60) + 0) : (h = f, c), this.parallaxTargX = (h - i / 2) / (o.parallaxMultiplier * this.layer), this.parallaxOffsetX += (this.parallaxTargX - this.parallaxOffsetX) / 10, this.parallaxTargY = (p - a / 2) / (o.parallaxMultiplier * this.layer), this.parallaxOffsetY += (this.parallaxTargY - this.parallaxOffsetY) / 10);
                var t = s.offsetWidth,
                    e = s.offsetHeight;
                switch (o.directionX) {
                    case "left":
                        this.position.x + this.speed.x + this.parallaxOffsetX < 0 && (this.position.x = t - this.parallaxOffsetX);
                        break;
                    case "right":
                        this.position.x + this.speed.x + this.parallaxOffsetX > t && (this.position.x = 0 - this.parallaxOffsetX);
                        break;
                    default:
                        (this.position.x + this.speed.x + this.parallaxOffsetX > t || this.position.x + this.speed.x + this.parallaxOffsetX < 0) && (this.speed.x = -this.speed.x)
                }
                switch (o.directionY) {
                    case "up":
                        this.position.y + this.speed.y + this.parallaxOffsetY < 0 && (this.position.y = e - this.parallaxOffsetY);
                        break;
                    case "down":
                        this.position.y + this.speed.y + this.parallaxOffsetY > e && (this.position.y = 0 - this.parallaxOffsetY);
                        break;
                    default:
                        (this.position.y + this.speed.y + this.parallaxOffsetY > e || this.position.y + this.speed.y + this.parallaxOffsetY < 0) && (this.speed.y = -this.speed.y)
                }
                this.position.x += this.speed.x, this.position.y += this.speed.y
            }, v.prototype.setStackPos = function(t) {
                this.stackPos = t
            },
            function() {
                if (l) {
                    (r = O.createElement("canvas")).className = "pg-canvas", r.style.display = "block", s.insertBefore(r, s.firstChild), n = r.getContext("2d"), g();
                    for (var t = Math.round(r.width * r.height / o.density), e = 0; e < t; e++) {
                        var i = new v;
                        i.setStackPos(e), d.push(i)
                    }
                    Y.addEventListener("resize", function() {
                        ! function() {
                            g();
                            for (var t = s.offsetWidth, e = s.offsetHeight, i = d.length - 1; 0 <= i; i--)(d[i].position.x > t || d[i].position.y > e) && d.splice(i, 1);
                            var a = Math.round(r.width * r.height / o.density);
                            if (a > d.length)
                                for (; a > d.length;) {
                                    var n = new v;
                                    d.push(n)
                                } else a < d.length && d.splice(a);
                            for (i = d.length - 1; 0 <= i; i--) d[i].setStackPos(i)
                        }()
                    }, !1), O.addEventListener("mousemove", function(t) {
                        f = t.pageX, c = t.pageY
                    }, !1), u && !x && Y.addEventListener("deviceorientation", function() {
                        y = Math.min(Math.max(-event.beta, -30), 30), m = Math.min(Math.max(-event.gamma, -30), 30)
                    }, !0), w(), X("onInit")
                }
            }(), {
                option: function(t, e) {
                    if (!e) return o[t];
                    o[t] = e
                },
                destroy: function() {
                    console.log("destroy"), r.parentNode.removeChild(r), X("onDestroy"), S && S(s).removeData("plugin_" + M)
                },
                start: function() {
                    e = !1, w()
                },
                pause: function() {
                    e = !0
                }
            }
    }
    Y[M] = function(t, e) {
        return new n(t, e)
    }, Y[M].defaults = {
        minSpeedX: .1,
        maxSpeedX: .7,
        minSpeedY: .1,
        maxSpeedY: .7,
        directionX: "center",
        directionY: "center",
        density: 1e4,
        dotColor: "#666666",
        lineColor: "#666666",
        particleRadius: 7,
        lineWidth: 1,
        curvedLines: !1,
        proximity: 100,
        parallax: !0,
        parallaxMultiplier: 5,
        onInit: function() {},
        onDestroy: function() {}
    }, S && (S.fn[M] = function(t) {
        if ("string" == typeof t) {
            var e, i = t,
                a = Array.prototype.slice.call(arguments, 1);
            return this.each(function() {
                S.data(this, "plugin_" + M) && "function" == typeof S.data(this, "plugin_" + M)[i] && (e = S.data(this, "plugin_" + M)[i].apply(this, a))
            }), void 0 !== e ? e : this
        }
        if ("object" == typeof t || !t) return this.each(function() {
            S.data(this, "plugin_" + M) || S.data(this, "plugin_" + M, new n(this, t))
        })
    })
   }(window, document),
   function() {
    for (var s = 0, t = ["ms", "moz", "webkit", "o"], e = 0; e < t.length && !window.requestAnimationFrame; ++e) window.requestAnimationFrame = window[t[e] + "RequestAnimationFrame"], window.cancelAnimationFrame = window[t[e] + "CancelAnimationFrame"] || window[t[e] + "CancelRequestAnimationFrame"];
    window.requestAnimationFrame || (window.requestAnimationFrame = function(t, e) {
        var i = (new Date).getTime(),
            a = Math.max(0, 16 - (i - s)),
            n = window.setTimeout(function() {
                t(i + a)
            }, a);
        return s = i + a, n
    }), window.cancelAnimationFrame || (window.cancelAnimationFrame = function(t) {
        clearTimeout(t)
    })
   }();
}