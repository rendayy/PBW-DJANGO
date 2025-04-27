const teamMembers = [
    {
        id: 1,
        name: "Mochammad Ramadhan Alfikri",
        title: "AMF",
        image: "/static/image/tim/093.png",
        description: "Saya AMF. Bisa nyerang ke depan (frontend), bisa bantu bertahan di belakang (backend). Fleksibel, adaptif, dan jago ngebaca arah permainan.",
        bio: "Seperti Attacking Midfielder di lapangan bola, saya ada di tengah—penghubung antara tampilan dan logika, antara kreativitas dan fungsionalitas. Kadang bantu cetak goal dengan UI yang manis, kadang turun bantu defense waktu ada bug yang nyelip diam-diam.Gak masalah dilempar ke frontend atau backend, saya enjoy dua-duanya. Styling layout kayak kasih umpan lambung ke sayap, logika program saya atur layaknya ngatur tempo dan arah permainan biar alur kerja tim tetap solid.Posisi: AMF (Aesthetic-Minded Fullstack )",
        email: "ramadhanalfikriimp@gmail.com",
        phone: "+62 88217222486",
        instagram: "https://www.instagram.com/mramadhan_a.f?igsh=MWs5bHplcmxxZGN6NA==",
        github: "https://github.com/ramadhan14123?tab=overview&from=2025-04-01&to=2025-04-24",
        IgUsername:"mramadhan_a.f"
    },
    {
        id: 2,
        name: "Haselinda Angelina Cahyani",
        title: "CF",
        image: "/static/image/tim/140.png",
        description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        bio: "Siti Rahma bergabung dengan Tim Kami pada tahun 2019 sebagai Lead Designer. Dengan keahliannya dalam UI/UX design, Siti telah membantu banyak klien dalam menciptakan pengalaman pengguna yang intuitif dan menarik. Siti memiliki latar belakang pendidikan di bidang Desain Komunikasi Visual dan telah memenangkan beberapa penghargaan desain nasional.",
        email: "haselindaaa@gmail.com",
        phone: "+62 812 3456 7891",
        instagram: "https://www.instagram.com/mramadhan_a.f?igsh=MWs5bHplcmxxZGN6NA==",
        github: "https://github.com/haselinda/",
        IgUsername:"Haselindaaa"
    },
    {
        id: 3,
        name: "Raihan Rizky Arsandi",
        title: "CMF",
        image: "/static/image/tim/104.png",
        description: "CMF. Kadang salah pass, kadang kena pressing bug langsung panik. Gak jago dribbling kodingan, tapi setia nemenin project sampe overtime.",
        bio: "Seperti Central Midfielder di lapangan bola, saya adalah pengatur ritme—penyeimbang antara soliditas dan kreativitas, antara disiplin struktur dan terobosan inovatif. Saya Bisa memegang peran sebagai anchor yang menjaga stabilitas sistem, sekaligus merangkap sebagai deep-lying organizer yang memastikan setiap pass kode tepat sasaran. Ketika serangan balik mendadak (bug muncul), saya yang pertama recover possession. Ketika tim butuh build-up (pengembangan fitur), saya yang jadi pivot-nya. Posisi: CMF (Code-Mindset Midfielder) - Bekerja di bawah radar, tapi semua serangan dan pertahanan bermula dari sini.",
        email: "bangrenac2@gmail.com",
        phone: "+62 812 3456 7892",
        instagram: "https://www.instagram.com/raihan_rz9?igsh=MXI0eWZhNHU1djI4dw==",
        github: "https://github.com/rendayy",
        IgUsername:"raihan_rz9"
    },
    {
        id: 4,
        name: "M.Zidan Kusuma Firdaus",
        title: "CMF",
        image: "/static/image/tim/078.png",
        description: "If you're having a bad day just remember.. IT'S YOUR FAULT.",
        bio: "Sebagai seorang CMF (Core-Minded Fullstack), saya adalah jantung yang ingin santai tapi tidak bisa. Fokus saya terletak pada jantung yang sehat, waktu istirahat yang terstruktur, dan performa yang andal. Saya memastikan pondasi backend sekuat baja dan alur data terintegrasi dengan mulus, menjadi otak di balik layar yang menjaga ritme proyek tetap stabil dan mengarahkannya pada fungsionalitas yang tak tergoyahkan melalui solusi efisien dan API yang terstruktur. SAYA INGIN ISTIRAHAT.",
        email: "zidankusumafirdaus.school@gmail.com",
        phone: "+62 812 3456 7893",
        instagram: "https://www.instagram.com/zidankusumafirdaus?igsh=MWFmaDBwcjlsazR6MA==",
        github: "https://github.com/zidankusumafirdaus",
        IgUsername:"zidankusumafirdaus"
    },
    {
        id: 5,
        name: "Rizky Nilamsari",
        title: "RWF",
        image: "/static/image/tim/091.png",
        description: "Right-Wing Freestyler. bisa diandelin, tapi kadang bawa kejutan. Kalo lagi bagus, aku MOTM. Kalo engga... yaudah lupa aja. ",
        bio: "Lari ngacir di flank kiri pas dibutuhin di kanan. Kadang nyetir sendirian sampe kehilangan arah, eh tau-telu bikin solusi random yang somehow ngebantu. Kreatif tapi inconsistent — kalo lagi on bisa bikin fitur keren dalam semalam, kalo off malah ngerusak styling yang udah bener. Paling jago improvisasi pas deadline mepet, tapi kalo disuruh ikut alur standar... yaudah deh aku diem aja.",
        email: "reza@example.com",
        phone: "+62 812 3456 7894",
        instagram: "https://www.instagram.com/jajanchiki08?igsh=dXJhcXVhNzM4dmtn",
        github: "https://github.com/kikik8",
        IgUsername:"jajanchika08"
    },
    {
        id: 6,
        name: "Muhammad Khansa Gian Ramanda",
        title: "CB",
        image: "/static/image/tim/154.png",
        description: "Bukan bintang tim, tapi kalo aku absen, semua kebobolan. Defender yang jago ngeyel: 'Ini harus di-fix dulu, baru lanjut! ",
        bio: "Aku mungkin nggak bikin fitur wow, tapi yang penting sistem aman. Gaya bermainku simpel: antisipasi bug sebelum jadi masalah, bongkar logic yang mencurigakan, dan bersihin technical debt kayak sweep bola mati. Reaktif? Iya. Elegan? Nggak selalu. Tapi kalo ada error yang nyerang, aku yang pertama nge-block.",
        email: "lina@example.com",
        phone: "+62 812 3456 7895",
        instagram: "https://www.instagram.com/ruphas_sama?igsh=MTZmbWhtY251YnFtMA==",
        github: "https://github.com/Rama-lab79",
        IgUsername:"ruphas_sama"
    },
{
        id: 7,
        name: "Achmad Arifin Nur H.",
        title: "GK",
        image: "/static/image/tim/noneMale.png",
        description: "Bukan yang tercepat, bukan yang terpintar, tapi paling rela jor-rodan di kubangan error 500 demi jaga gawang tetap clean sheet.",
        bio: "Tim kebobolan? Mentalku mental pantang down. Kena hattrick error di production? Bangun lagi, commit lagi. Aku mungkin sering salah baca spec, tapi selalu siap jadi last line of defense - paling jago berantem sama bug critical yang udah terlanjur lolos ke live. Kalo ada yang bilang 'ini mustahil di-fix', justru itu saatnya aku shine (sambil nangis dikit)",
        email: "lina@example.com",
        phone: "+62 812 3456 7895",
        instagram: "",
        github: "https://github.com/ArFn24",
        IgUsername:"Blank@gmail.com"
    },

{
        id: 8,
        name: "Tita Lintang Ingrid. T",
        title: "LWF",
        image: "/static/image/tim/None.png",
        description: "Winger yang unpredictable - bisa MVP bisa jadi beban, tergantung hari dan kadar kopi.",
        bio: "Sprint kencang pas awal project, 90 menit ngos-ngosan di tengah jalan. Kadang cut inside bikin solusi kreatif, kadang nyasar ke stackoverflow sampe lupa masalah awalnya apa. Kalo lagi mood bisa solo carry fitur kompleks, kalo engga... 'Bro, nanti aku deploynya besok... eh maksudnya minggu depan.",
        email: "lina@example.com",
        phone: "+62 812 3456 7895",
        instagram: "https://www.instagram.com/lintangg.ngd?igsh=ZXl3Y2Q2YWZqcXU5",
        github: "https://github.com/lintang88",
        IgUsername:"lintang.ngd"
    }
];

// Fungsi untuk menampilkan tim
function displayTeam() {
    const teamGrid = document.getElementById('team-grid');
    
    teamMembers.forEach(member => {
        const teamCard = document.createElement('div');
        teamCard.className = 'team-card';
        teamCard.setAttribute('data-id', member.id);
        
        teamCard.innerHTML = `
            <img src="${member.image}" alt="${member.name}" class="team-img">
            <div class="team-info">
                <h3 class="team-name">${member.name}</h3>
                <p class="team-title">${member.title}</p>
                <p class="team-desc">${member.description}</p>
                <div class="team-social">
                    <a href="${member.instagram || '#'}" class="social-icon" target="_blank" title="instagram"><i class="fab fa-instagram"></i></a>
                    <a href="${member.github}" class="social-icon" target="_blank" title="GitHub"><i class="fab fa-github"></i></a>
                    <a href="mailto:${member.email}" class="social-icon"> <i class="fas fa-envelope"></i></a>
                </div>
            </div>
        `;
        
        teamGrid.appendChild(teamCard);

        // Menambahkan event listener untuk membuka modal
        teamCard.addEventListener('click', () => openModal(member.id));
    });
}



// Fungsi untuk membuka modal
function openModal(memberId) {
    const member = teamMembers.find(m => m.id === memberId);
    
    if (member) {
        document.getElementById('modal-img').src = member.image;
        document.getElementById('modal-name').textContent = member.name;
        document.getElementById('modal-title').textContent = member.title;
        document.getElementById('modal-bio').textContent = member.bio;
        document.getElementById('modal-email').textContent = member.email;
        document.getElementById('modal-IgUsername').textContent = member.IgUsername;

        const igLink = document.getElementById('modal-IgUsername');
        if (member.instagram && member.IgUsername) {
            igLink.href = member.instagram;
            igLink.textContent = `${member.IgUsername}`;
            igLink.style.display = 'inline';
        } else {
            igLink.style.display = 'none';
        }

        
        document.getElementById('team-modal').style.display = 'flex';
        
    }
}


// Fungsi untuk menutup modal
function closeModal() {
    document.getElementById('team-modal').style.display = 'none';
}

// Toggle menu mobile
function toggleMenu() {
    const navLinks = document.getElementById('nav-links');
    navLinks.classList.toggle('active');
}


// Event listeners
document.addEventListener('DOMContentLoaded', () => {
    displayTeam();
    
    // Close modal
    document.getElementById('close-modal').addEventListener('click', closeModal);
    
    // Click outside modal to close
    document.getElementById('team-modal').addEventListener('click', (e) => {
        if (e.target === document.getElementById('team-modal')) {
            closeModal();
        }
    });
    
    // Hamburger menu
    document.getElementById('hamburger-btn').addEventListener('click', toggleMenu);
});

// Particles
document.addEventListener('DOMContentLoaded', function() {
    if (document.getElementById('particles-js')) {
        particlesJS('particles-js', {
            "particles": {
                "number": {
                    "value": 120,           // Menambah jumlah partikel
                    "density": {
                        "enable": true,
                        "value_area": 800
                    }
                },
                "color": {
                },
                "shape": {
                    "type": "circle",
                    "stroke": {
                        "width": 1,         
                        "color": "#D4E1DF"  
                    }
                },
                "opacity": {
                    "value": 0.6,          
                    "random": true,
                    "anim": {
                        "enable": true,
                        "speed": 1,
                        "opacity_min": 0.3, 
                        "sync": false
                    }
                },
                "size": {
                    "value": 2,             // Ukuran partikel lebih besar
                    "random": true,
                    "anim": {
                        "enable": true,      // Animasi ukuran diaktifkan
                        "speed": 3,
                        "size_min": 2,
                        "sync": false
                    }
                },
                "line_linked": {
                    "enable": true,
                    "distance": 150,
                    "color": "#71BCA8",     
                    "opacity": 0.5,         
                    "width": 1.5            
                },
                "move": {
                    "enable": true,
                    "speed": 3,             
                    "direction": "none",
                    "random": true,
                    "straight": false,
                    "out_mode": "bounce",   
                    "bounce": true,
                    "attract": {
                        "enable": true,     
                        "rotateX": 600,
                        "rotateY": 1200
                    }
                }
            },
            "interactivity": {
                "detect_on": "canvas",
                "events": {
                    "onhover": {
                        "enable": true,
                        "mode": "grab"     
                    },
                    "onclick": {
                        "enable": true,
                        "mode": "push"      
                    },
                    "resize": true
                },
                "modes": {
                    "grab": {
                        "distance": 180,    
                        "line_linked": {
                            "opacity": 0.4  
                        }
                    },
                    "bubble": {
                        "distance": 200,
                        "size": 12,
                        "duration": 2,
                        "opacity": 0.8,
                        "speed": 3
                    },
                    "repulse": {
                        "distance": 150,    
                        "duration": 0.4
                    },
                    "push": {
                        "particles_nb": 6   
                    },
                    "remove": {
                        "particles_nb": 2
                    }
                }
            },
            "retina_detect": true
        });
        console.log('Particles.js initialized successfully!'); 
    } else {
        console.error('Particles container not found!'); 
    }
});