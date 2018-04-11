#include <linux/module.h>
#include <linux/vermagic.h>
#include <linux/compiler.h>

MODULE_INFO(vermagic, VERMAGIC_STRING);

__visible struct module __this_module
__attribute__((section(".gnu.linkonce.this_module"))) = {
	.name = KBUILD_MODNAME,
	.init = init_module,
#ifdef CONFIG_MODULE_UNLOAD
	.exit = cleanup_module,
#endif
	.arch = MODULE_ARCH_INIT,
};

static const struct modversion_info ____versions[]
__used
__attribute__((section("__versions"))) = {
	{ 0xd29ace7d, __VMLINUX_SYMBOL_STR(module_layout) },
	{ 0x3ce4ca6f, __VMLINUX_SYMBOL_STR(disable_irq) },
	{ 0xf9a482f9, __VMLINUX_SYMBOL_STR(msleep) },
	{ 0x44b1c7de, __VMLINUX_SYMBOL_STR(param_ops_int) },
	{ 0x2e5810c6, __VMLINUX_SYMBOL_STR(__aeabi_unwind_cpp_pr1) },
	{ 0x5d153a7a, __VMLINUX_SYMBOL_STR(hrtimer_active) },
	{ 0xfe009c06, __VMLINUX_SYMBOL_STR(hrtimer_forward) },
	{ 0x11025677, __VMLINUX_SYMBOL_STR(hrtimer_cancel) },
	{ 0x47229b5c, __VMLINUX_SYMBOL_STR(gpio_request) },
	{ 0x3d9835a6, __VMLINUX_SYMBOL_STR(gpio_to_desc) },
	{ 0xc87c1f84, __VMLINUX_SYMBOL_STR(ktime_get) },
	{ 0xb1ad28e0, __VMLINUX_SYMBOL_STR(__gnu_mcount_nc) },
	{ 0x9f0e1221, __VMLINUX_SYMBOL_STR(tty_register_driver) },
	{ 0x2f1f8f20, __VMLINUX_SYMBOL_STR(mutex_unlock) },
	{ 0xea7338ce, __VMLINUX_SYMBOL_STR(put_tty_driver) },
	{ 0xb130d89c, __VMLINUX_SYMBOL_STR(tty_set_operations) },
	{ 0x9955a327, __VMLINUX_SYMBOL_STR(hrtimer_start_range_ns) },
	{ 0xf10ae7ba, __VMLINUX_SYMBOL_STR(__tty_insert_flip_char) },
	{ 0xf090eadf, __VMLINUX_SYMBOL_STR(__mutex_init) },
	{ 0x27e1a049, __VMLINUX_SYMBOL_STR(printk) },
	{ 0x908f9da6, __VMLINUX_SYMBOL_STR(tty_port_init) },
	{ 0x9138e27f, __VMLINUX_SYMBOL_STR(mutex_lock) },
	{ 0x137c3884, __VMLINUX_SYMBOL_STR(gpiod_direction_input) },
	{ 0xd6687bfa, __VMLINUX_SYMBOL_STR(gpiod_direction_output_raw) },
	{ 0xd6b8e852, __VMLINUX_SYMBOL_STR(request_threaded_irq) },
	{ 0x2196324, __VMLINUX_SYMBOL_STR(__aeabi_idiv) },
	{ 0xfc33de0a, __VMLINUX_SYMBOL_STR(gpiod_set_debounce) },
	{ 0x67b27ec1, __VMLINUX_SYMBOL_STR(tty_std_termios) },
	{ 0xd1b3b4d0, __VMLINUX_SYMBOL_STR(tty_unregister_driver) },
	{ 0xfc66b74d, __VMLINUX_SYMBOL_STR(__tty_alloc_driver) },
	{ 0xfe990052, __VMLINUX_SYMBOL_STR(gpio_free) },
	{ 0x409873e3, __VMLINUX_SYMBOL_STR(tty_termios_baud_rate) },
	{ 0xfcec0987, __VMLINUX_SYMBOL_STR(enable_irq) },
	{ 0x6579d946, __VMLINUX_SYMBOL_STR(tty_port_link_device) },
	{ 0x64b35483, __VMLINUX_SYMBOL_STR(gpiod_to_irq) },
	{ 0x88260901, __VMLINUX_SYMBOL_STR(gpiod_set_raw_value) },
	{ 0x192441c6, __VMLINUX_SYMBOL_STR(hrtimer_init) },
	{ 0x913ab6e5, __VMLINUX_SYMBOL_STR(tty_flip_buffer_push) },
	{ 0xcf08282d, __VMLINUX_SYMBOL_STR(gpiod_get_raw_value) },
	{ 0xf20dabd8, __VMLINUX_SYMBOL_STR(free_irq) },
};

static const char __module_depends[]
__used
__attribute__((section(".modinfo"))) =
"depends=";


MODULE_INFO(srcversion, "2BD0C9CCF6F33AA0EC52A2B");
