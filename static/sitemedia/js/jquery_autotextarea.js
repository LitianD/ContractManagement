(function(a){a.fn.autoTextarea=function(b){var d={maxHeight:null,minHeight:a(this).height()};var c=a.extend({},d,b);return a(this).each(function(){a(this).bind("paste cut keydown keyup focus blur change",function(){var e,f=this.style;this.style.height=c.minHeight+"px";if(this.scrollHeight>c.minHeight){if(c.maxHeight&&this.scrollHeight>c.maxHeight){e=c.maxHeight;f.overflowY="scroll"}else{e=this.scrollHeight;f.overflowY="hidden"}f.height=e+"px"}})})}})(jQuery);$.fn.autoTextareaHeight=function(a){var b=this;$(window).on("resize.textarea-auto-height",function(){b.trigger("autoheighthandller")});return this.each(function(){var d=$(this);if(!d.data("origin-height")){d.data("origin-height",d.height())}var c=d[0].scrollHeight;if(d.height()!==c){d.height(c)}d.on("input keyup paste cut autoheighthandller",function(g){d.height(d.data("origin-height"));var f=d[0].scrollHeight;if(d.height()!==f){d.height(f)}})})};